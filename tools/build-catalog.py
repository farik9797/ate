#!/usr/bin/env python3
"""Генерирует каталог: страницы товаров product/*.html и раскрывающиеся категории в katalog.html.

Вход:  data/espa-raw.json (tools/scrape-espa.py), tools/catalog_data.py (переводы, Hidrostal).
Выход: product/espa-*.html, product/hidrostal-*.html, блоки <!-- gen:espa --> и <!-- gen:hidrostal -->
       в katalog.html, data/catalog.json (нормализованные данные для WP/WooCommerce).

Запуск:  python3 tools/build-catalog.py
Шапка/футер берутся из index.html (блоки chrome:*), как в tools/sync-chrome.py.
"""
import html
import json
import math
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import catalog_data as CD  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://farik9797.github.io/ate/"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
E = html.escape
PALETTE = ["#1E62D0", "#008AC7", "#15B3A6", "#1D3C8D", "#5B8DEF", "#0B6E99", "#7FB2F0", "#2C4A7A", "#3FBFE0", "#8C9EC9"]


# ------------------------------------------------------------------ helpers
def num(s):
    try:
        return float(str(s).replace(",", ".").split("/")[0])
    except ValueError:
        return None


def fmt(x, nd=1):
    if x is None:
        return ""
    s = f"{x:.{nd}f}".rstrip("0").rstrip(".") if nd else f"{x:.0f}"
    return s.replace(".", ",")


def tr_val(v):
    v = v.strip()
    if v in CD.VALUES:
        return CD.VALUES[v]
    m = re.fullmatch(r"Min: (-?[\d,.]+) - Max: (-?[\d,.]+)", v)
    if m:
        return f"от {m.group(1)} до {m.group(2)}"
    m = re.fullmatch(r"Max: (-?[\d,.]+)", v)
    if m:
        return f"до {m.group(1)}"
    m = re.fullmatch(r"([\d,.]+)mm", v)
    if m:
        return f"{m.group(1)} мм"
    return v


def tr_head(h):
    label, _, span = h.partition("|")
    label = label.strip()
    out = CD.TABLE_HEADS.get(label)
    if out is None:
        out = re.sub(r"(\d)V\b", r"\1 В", label)
    return out, int(span) if span else 1


def chrome_blocks():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    out = {}
    for b in ("head", "top", "footer", "bottom"):
        m = re.search(r"<!-- chrome:%s -->(.*?)<!-- /chrome:%s -->" % (b, b), src, re.S)
        out[b] = m.group(1)
    return out


def download(url, dest):
    if os.path.exists(dest):
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=40) as r, open(dest, "wb") as f:
            f.write(r.read())
        return True
    except Exception as e:  # noqa: BLE001
        print("  ! image failed", url, e, file=sys.stderr)
        return False


# ------------------------------------------------------------------ ESPA normalise
def doc_label(url):
    f = url.split("/")[-1].lower()
    for key, label in CD.DOC_TYPES:
        if key in f:
            return label
    return "Документ"


def espa_products(raw):
    cats = {k: (t, d) for k, t, d in CD.ESPA_CATEGORIES}
    out = []
    for p in raw:
        sub = CD.SUBTITLES.get(p["subtitle"], p["subtitle"])
        desc = [CD.DESCRIPTIONS.get(x, x) for x in p["description"]]
        feats = []
        for g in p["features"]:
            items = [[CD.KEYS.get(k, k), tr_val(v)] for k, v in g["items"] if v.strip()]
            if items:
                feats.append({"title": CD.GROUPS.get(g["title"], g["title"]), "items": items})
        # electrical table
        table = None
        p2 = []
        nmodels = 0
        if p["tables"]:
            t = p["tables"][0]
            head = [[tr_head(h) for h in row] for row in t["head"]]
            row1 = [h for h, _ in head[0]] if head else []
            n_model_cols = sum(1 for lbl in row1 if "модели" in lbl)
            flat2 = [h for h, _ in head[1]] if len(head) > 1 else []
            kw_idx = flat2.index("кВт") if "кВт" in flat2 else None
            extra = []
            for key, label in (("Pressure range", "Диапазон напора, м"), ("Maximum working pressure", "Макс. давление, бар"),
                               ("Maximum submersion", "Макс. погружение, м")):
                if any(key in lims for lims in p["models"].values()):
                    extra.append((key, label))
            rows = []
            for r in t["rows"]:
                models = [c for c in r[:n_model_cols] if c]
                nmodels += len(models)
                lims = next((p["models"][m] for m in models if m in p["models"]), {})
                cells = [c if c else "—" for c in r] + [lims.get(k, "—").replace(".", ",").replace("-", "–") for k, _ in extra]
                rows.append(cells)
                if kw_idx is not None and kw_idx < len(r):
                    v = num(r[kw_idx])
                    if v:
                        p2.append(v)
            table = {"head": head, "extra": [lbl for _, lbl in extra], "rows": rows}
        curves = {}
        for k, pts in p["curves"].items():
            label = (p["name"].upper() + (" " + k if k else "")).strip()
            curves[label] = pts
        allpts = [pt for c in curves.values() for pt in c]
        kpi = {
            "q": f"до {fmt(max(x for x, _ in allpts))} м³/ч" if allpts else "",
            "h": f"до {fmt(max(y for _, y in allpts), 0)} м" if allpts else "",
            "p": (f"{fmt(min(p2), 2)}–{fmt(max(p2), 2)} кВт" if min(p2) != max(p2) else f"{fmt(p2[0], 2)} кВт") if p2 else "",
            "models": nmodels,
        }
        docs, certs, seen = [], [], set()
        for u in p["docs"]:
            lbl = doc_label(u)
            if ("Pool" in lbl) != (p["category"] == "basseyny") and lbl.startswith(("Каталог", "Технический каталог")):
                continue  # каталог бассейнов — только для насосов для бассейнов, общий — для остальных
            if lbl == "Сертификат":
                certs.append(u)
                continue
            if lbl in seen:
                continue
            seen.add(lbl)
            docs.append((lbl, u))
        cat_t, _ = cats[p["category"]]
        out.append({
            "brand": "espa", "slug": p["slug"], "file": f"product/espa-{p['slug']}.html",
            "name": p["name"], "full_name": f"ESPA {p['name']}", "category": p["category"], "category_title": cat_t,
            "subtitle": sub, "description": desc, "features": feats, "table": table, "curves": curves, "kpi": kpi,
            "docs": docs, "certs": certs, "image": p["image_local"], "source": p["source"],
            "direction": "water-disposal" if p["category"] == "drenazh" else "water-supply",
            "highlights": [], "applications": [], "specs": [],
        })
    return out


def hidrostal_products():
    cats = {k: (t, d) for k, t, d in CD.HIDROSTAL_CATEGORIES}
    imgdir = os.path.join(ROOT, "assets", "img", "products", "hidrostal")
    os.makedirs(imgdir, exist_ok=True)
    out = []
    for h in CD.HIDROSTAL:
        ext = os.path.splitext(h["image_src"])[1].lower() or ".jpg"
        rel = f"assets/img/products/hidrostal/{h['slug']}{ext}"
        ok = download(h["image_src"], os.path.join(ROOT, rel))
        out.append({
            "brand": "hidrostal", "slug": h["slug"], "file": f"product/hidrostal-{h['slug']}.html",
            "name": h["short"], "full_name": h["name"], "category": h["category"], "category_title": cats[h["category"]][0],
            "subtitle": h["subtitle"], "description": h["description"], "features": [], "table": None, "curves": {},
            "kpi": {**h["kpi"], "models": 0}, "docs": h["docs"], "certs": [], "image": rel if ok else "",
            "source": h["page"], "direction": "water-disposal",
            "highlights": h["highlights"], "applications": h["applications"], "specs": h["specs"],
        })
    return out


# ------------------------------------------------------------------ chart
def nice_max(v):
    if v <= 0:
        return 1
    e = 10 ** math.floor(math.log10(v))
    for m in (1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10):
        if v <= m * e:
            return m * e
    return 10 * e


def chart_svg(curves):
    W, H, L, R, T, B = 760, 380, 58, 18, 16, 48
    pts = [pt for c in curves.values() for pt in c]
    xmax, ymax = nice_max(max(x for x, _ in pts)), nice_max(max(y for _, y in pts))
    sx = lambda x: L + (W - L - R) * x / xmax  # noqa: E731
    sy = lambda y: T + (H - T - B) * (1 - y / ymax)  # noqa: E731
    g = []
    for i in range(6):
        xv, yv = xmax * i / 5, ymax * i / 5
        g.append(f'<line x1="{sx(xv):.1f}" y1="{T}" x2="{sx(xv):.1f}" y2="{H-B}" class="ch-grid"/>')
        g.append(f'<line x1="{L}" y1="{sy(yv):.1f}" x2="{W-R}" y2="{sy(yv):.1f}" class="ch-grid"/>')
        g.append(f'<text x="{sx(xv):.1f}" y="{H-B+18}" text-anchor="middle" class="ch-tick">{fmt(xv, 2)}</text>')
        g.append(f'<text x="{L-8}" y="{sy(yv)+4:.1f}" text-anchor="end" class="ch-tick">{fmt(yv, 1)}</text>')
    g.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-8}" text-anchor="middle" class="ch-ax">Подача Q, м³/ч</text>')
    g.append(f'<text transform="translate(16 {(T+H-B)/2:.0f}) rotate(-90)" text-anchor="middle" class="ch-ax">Напор H, м</text>')
    legend = []
    for i, (name, c) in enumerate(curves.items()):
        col = PALETTE[i % len(PALETTE)]
        d = "M" + " L".join(f"{sx(x):.1f} {sy(y):.1f}" for x, y in sorted(c))
        g.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"><title>{E(name)}</title></path>')
        legend.append(f'<li><span class="ch-sw" style="background:{col}"></span>{E(name)}</li>')
    svg = (f'<svg viewBox="0 0 {W} {H}" class="chart" role="img" aria-label="Кривые Q–H, 50 Гц">'
           f'<rect x="{L}" y="{T}" width="{W-L-R}" height="{H-T-B}" class="ch-bg"/>{"".join(g)}</svg>')
    return svg + f'<ul class="ch-legend">{"".join(legend)}</ul>'


# ------------------------------------------------------------------ html parts
ICON_ARROW = '<svg class="ic ic-arrow" aria-hidden="true"><use href="#i-arrow-right"/></svg>'


def kpi_chips(p):
    k = p["kpi"]
    parts = []
    if k.get("q"):
        parts.append(f"Q {k['q']}")
    if k.get("h"):
        parts.append(f"H {k['h']}")
    if k.get("p"):
        parts.append(("P2 " if p["brand"] == "espa" else "P ") + k["p"])
    return "".join(f"<span>{E(x)}</span>" for x in parts)


def card(p):
    img = (f'<img src="{E(p["image"])}" alt="{E(p["full_name"])}" loading="lazy">' if p["image"]
           else '<span class="pcard-noimg">Фото по запросу</span>')
    chips = kpi_chips(p)
    return (f'<a class="pcard" href="{E(p["file"])}">'
            f'<span class="pcard-img">{img}</span>'
            f'<span class="pcard-body"><span class="pcard-brand">{"ESPA" if p["brand"]=="espa" else "Hidrostal"}</span>'
            f'<span class="pcard-t">{E(p["name"])}</span>'
            f'<span class="pcard-s">{E(p["subtitle"])}</span>'
            f'{"<span class=pcard-kpi>"+chips+"</span>" if chips else ""}'
            f'<span class="pcard-link">Тех. характеристики {ICON_ARROW}</span></span></a>')


def accordion(brand, categories, products, open_first=True):
    out = []
    for i, (key, title, desc) in enumerate(categories, 1):
        items = [p for p in products if p["category"] == key]
        if not items:
            continue
        n = len(items)
        word = "серия" if n % 10 == 1 and n % 100 != 11 else "серии" if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else "серий"
        out.append(
            f'<details class="acc" id="{brand}-{key}"{" open" if (open_first and i == 1) else ""}>'
            f'<summary class="acc-sum"><span class="acc-num">{i:02d}</span>'
            f'<span class="acc-tt"><span class="acc-t">{E(title)}</span><span class="acc-s">{E(desc)} · {n} {word}</span></span>'
            f'<span class="acc-ic" aria-hidden="true"><svg class="ic"><use href="#i-chevron-down"/></svg></span></summary>'
            f'<div class="acc-body"><div class="pgrid">{"".join(card(p) for p in items)}</div></div></details>')
    return "\n".join(out)


def table_html(t):
    head = t["head"]
    rows_html = []
    for ri, row in enumerate(head):
        ths = []
        for label, span in row:
            ths.append(f'<th{" colspan=%d" % span if span > 1 else ""}>{E(label)}</th>')
        if ri == 0:
            ths += [f'<th rowspan="{len(head)}">{E(x)}</th>' for x in t["extra"]]
        rows_html.append("<tr>" + "".join(ths) + "</tr>")
    body = "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in r) + "</tr>" for r in t["rows"])
    return f'<div class="tbl-wrap"><table class="spec-table"><thead>{"".join(rows_html)}</thead><tbody>{body}</tbody></table></div>'


def product_page(p, related, chrome):
    brand_name = "ESPA" if p["brand"] == "espa" else "Hidrostal"
    logo = ('<img src="assets/logo/espa.png?v=3" alt="ESPA" class="h-9 w-auto" width="115" height="36">' if p["brand"] == "espa"
            else '<img src="assets/logo/hidrostal-blue.png?v=3" alt="Hidrostal" class="h-8 w-auto" width="134" height="32">')
    cat_anchor = f'katalog.html#{p["brand"]}-{p["category"]}'
    short_sub = p["subtitle"].split(",")[0].rstrip(".")
    title = (f'{p["full_name"]} — {short_sub[:1].lower() + short_sub[1:]} | ТОО «АТЕ»' if p["brand"] == "espa"
             else f'{p["full_name"]}: характеристики и документация | ТОО «АТЕ»')
    k = p["kpi"]
    kparts = [x for x in (("подача " + k["q"]) if k.get("q") else "", ("напор " + k["h"]) if k.get("h") else "",
                          ("мощность " + k["p"]) if k.get("p") else "") if x]
    meta = f'{p["full_name"]}: {p["subtitle"].rstrip(".")}' + (f' ({", ".join(kparts)})' if kparts else "") + \
        f'. Технические характеристики, документация, подбор и поставка в Казахстане — ТОО «АТЕ», официальный представитель {brand_name}.'
    url = SITE + p["file"]
    img_abs = SITE + p["image"] if p["image"] else SITE + "assets/img/hero-astana.jpg"

    tiles = []
    for label, val in (("Макс. подача", k.get("q")), ("Макс. напор", k.get("h")),
                       ("Мощность P2" if p["brand"] == "espa" else "Мощность", k.get("p")),
                       ("Моделей в серии", str(k["models"]) if k.get("models") else "")):
        if val:
            tiles.append(f'<div class="kpi"><dt>{E(label)}</dt><dd>{E(val)}</dd></div>')

    sections, tabs = [], []

    def sec(sid, title_, body, gray=False):
        tabs.append((sid, title_))
        sections.append(f'<section id="{sid}" class="psec{" bg-sky-3" if gray else ""}"><div class="wrap">'
                        f'<h2 class="h-sec">{E(title_)}</h2>{body}</div></section>')

    # description
    body = "".join(f"<p>{E(x)}</p>" for x in p["description"])
    if p["highlights"]:
        body += '<h3 class="psub">Особенности</h3><ul class="checks">' + "".join(f"<li>{E(x)}</li>" for x in p["highlights"]) + "</ul>"
    if p["applications"]:
        body += '<h3 class="psub">Применение</h3><ul class="tags">' + "".join(f"<li>{E(x)}</li>" for x in p["applications"]) + "</ul>"
    sec("opisanie", "Описание и применение", f'<div class="prose mt-6 max-w-[860px]">{body}</div>')

    # characteristics
    groups = list(p["features"])
    if p["specs"]:
        groups = [{"title": "Основные параметры", "items": [list(x) for x in p["specs"]]}] + groups
    if groups:
        cols = "".join(
            f'<div class="fgroup"><h3 class="fgroup-t">{E(g["title"])}</h3><dl class="spec-dl">'
            + "".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a, b in g["items"]) + "</dl></div>" for g in groups)
        sec("harakteristiki", "Технические характеристики", f'<div class="fgrid mt-8">{cols}</div>', gray=True)

    if p["table"]:
        sec("modeli", "Модели и электрические данные",
            '<p class="pnote">Данные для 50 Гц. На мобильном таблица прокручивается по горизонтали.</p>' + table_html(p["table"]))

    if p["curves"]:
        sec("krivye", "Рабочие характеристики Q–H",
            '<p class="pnote">Кривые напора по моделям серии, 50 Гц. Источник — технические данные производителя.</p>'
            f'<div class="chart-wrap">{chart_svg(p["curves"])}</div>', gray=bool(p["table"]))

    docs = "".join(f'<li><a href="{E(u)}" target="_blank" rel="noopener"><svg class="ic" aria-hidden="true"><use href="#i-file-text"/></svg>'
                   f'<span>{E(lbl)}</span><svg class="ic ic-sm" aria-hidden="true"><use href="#i-download"/></svg></a></li>' for lbl, u in p["docs"])
    if p["certs"]:
        docs += ('<li class="doc-certs"><svg class="ic" aria-hidden="true"><use href="#i-shield-check"/></svg><span>Сертификаты: '
                 + " · ".join(f'<a href="{E(u)}" target="_blank" rel="noopener">{i}</a>' for i, u in enumerate(p["certs"], 1)) + "</span></li>")
    docs += (f'<li><a href="{E(p["source"])}" target="_blank" rel="noopener"><svg class="ic" aria-hidden="true"><use href="#i-external-link"/></svg>'
             f'<span>Страница серии на сайте {brand_name}</span></a></li>')
    sec("dokumenty", "Документация", f'<ul class="doc-list mt-6">{docs}</ul>')

    rel_cards = "".join(card(r) for r in related[:4])
    related_html = (f'<section class="psec bg-sky-3"><div class="wrap"><div class="flex flex-wrap items-end justify-between gap-4">'
                    f'<h2 class="h-sec">Другие серии в категории</h2><a href="{E(cat_anchor)}" class="btn btn-primary">Вся категория {ICON_ARROW}</a></div>'
                    f'<div class="pgrid mt-8">{rel_cards}</div></div></section>') if rel_cards else ""

    tabs_html = "".join(f'<a href="{E(p["file"])}#{sid}">{E(t)}</a>' for sid, t in tabs)
    popup = (f'data-popup="lead" data-popup-title="Запросить подбор: {E(p["full_name"])}" data-popup-dir="{p["direction"]}" '
             f'data-popup-note="Интересует: {E(p["full_name"])}"')
    manual = next((u for lbl, u in p["docs"] if lbl.startswith("Инструкция") or lbl.startswith("Брошюра")), None)
    manual_btn = (f'<a href="{E(manual)}" target="_blank" rel="noopener" class="link-ghost">'
                  f'{"Инструкция PDF" if p["brand"]=="espa" else "Брошюра PDF"} <svg class="ic ic-sm" aria-hidden="true"><use href="#i-download"/></svg></a>') if manual else ""
    img = (f'<img src="{E(p["image"])}" alt="{E(p["full_name"])}" width="600" height="600">' if p["image"]
           else '<span class="pcard-noimg">Фото по запросу</span>')

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Product", "name": p["full_name"], "brand": {"@type": "Brand", "name": brand_name},
             "description": p["subtitle"], "image": img_abs, "category": p["category_title"], "url": url},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Главная", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": "Каталог", "item": SITE + "katalog.html"},
                {"@type": "ListItem", "position": 3, "name": p["category_title"], "item": SITE + cat_anchor},
                {"@type": "ListItem", "position": 4, "name": p["full_name"], "item": url}]},
        ],
    }
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<base href="../">
<title>{E(title)}</title>
<meta name="description" content="{E(meta)}">
<meta property="og:type" content="product">
<meta property="og:site_name" content="ТОО «АТЕ»">
<meta property="og:locale" content="ru_RU">
<meta property="og:title" content="{E(p['full_name'])}">
<meta property="og:description" content="{E(p['subtitle'])}">
<meta property="og:url" content="{E(url)}">
<meta property="og:image" content="{E(img_abs)}">
<link rel="canonical" href="{E(url)}">
<meta name="theme-color" content="#0B1F3A">
<link rel="icon" type="image/svg+xml" href="favicon.svg?v=6">
<link rel="icon" type="image/png" sizes="64x64" href="favicon.png?v=6">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png?v=6">
<link rel="apple-touch-icon" href="apple-touch-icon.png?v=6">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<!-- chrome:head -->{chrome['head']}<!-- /chrome:head -->
</head>
<body class="font-body text-ink" data-nav="katalog.html">
<!-- chrome:top -->{chrome['top']}<!-- /chrome:top -->

<main id="top">

<section class="prod-hero">
  <div class="wrap">
    <ol class="crumbs crumbs-dark" aria-label="Навигация по сайту">
      <li><a href="index.html">Главная</a></li>
      <li><a href="katalog.html">Каталог</a></li>
      <li><a href="katalog.html#{p['brand']}">{brand_name}</a></li>
      <li><a href="{E(cat_anchor)}">{E(p['category_title'])}</a></li>
      <li>{E(p['name'])}</li>
    </ol>
    <div class="grid lg:grid-cols-[minmax(0,5fr)_minmax(0,7fr)] gap-8 lg:gap-14 items-center">
      <div class="prod-img">{img}</div>
      <div>
        <div class="flex items-center gap-4 flex-wrap">{logo}<span class="eyebrow">{E(p['category_title'])}</span></div>
        <h1 class="h-page text-navy mt-5">{E(p['full_name'])}</h1>
        <p class="lead !text-ink-2 !mt-4">{E(p['subtitle'])}</p>
        {'<dl class="kpis">' + ''.join(tiles) + '</dl>' if tiles else ''}
        <div class="mt-8 flex flex-wrap items-center gap-x-6 gap-y-4">
          <a href="kontakty.html" {popup} class="btn btn-primary">Запросить подбор и цену {ICON_ARROW}</a>
          {manual_btn}
        </div>
      </div>
    </div>
  </div>
</section>

<nav class="prod-tabs" aria-label="Разделы товара"><div class="wrap">{tabs_html}</div></nav>

{''.join(sections)}

{related_html}

<section class="psec bg-white">
  <div class="wrap">
    <p class="src-note">Технические данные — из каталога и документации производителя {brand_name} (<a href="{E(p['source'])}" target="_blank" rel="noopener">источник</a>). Перед заказом уточняйте исполнение и комплектацию у инженера ТОО «АТЕ». Цена — по запросу.</p>
    <div class="cta-band rv mt-8">
      <div>
        <h2 class="font-display font-bold text-[24px] md:text-[30px] leading-tight">Подберём модель под ваш объект</h2>
        <p class="mt-2 text-white/75">Пришлите расход, напор и условия монтажа — подготовим технико-коммерческое предложение.</p>
      </div>
      <a href="kontakty.html" {popup} class="btn btn-primary">Оставить заявку {ICON_ARROW}</a>
    </div>
  </div>
</section>

</main>

<!-- chrome:footer -->{chrome['footer']}<!-- /chrome:footer -->
<!-- chrome:bottom -->{chrome['bottom']}<!-- /chrome:bottom -->
</body>
</html>
"""


# ------------------------------------------------------------------ main
def replace_block(text, name, content):
    pat = re.compile(r"(<!-- gen:%s -->).*?(<!-- /gen:%s -->)" % (name, name), re.S)
    if not pat.search(text):
        raise SystemExit(f"katalog.html: нет маркеров gen:{name}")
    return pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), text)


def main():
    raw = json.load(open(os.path.join(ROOT, "data", "espa-raw.json"), encoding="utf-8"))
    espa = espa_products(raw)
    hidro = hidrostal_products()
    allp = espa + hidro
    chrome = chrome_blocks()
    os.makedirs(os.path.join(ROOT, "product"), exist_ok=True)
    for p in allp:
        related = [r for r in allp if r["brand"] == p["brand"] and r["category"] == p["category"] and r["slug"] != p["slug"]]
        with open(os.path.join(ROOT, p["file"]), "w", encoding="utf-8") as f:
            f.write(product_page(p, related, chrome))
    kat = os.path.join(ROOT, "katalog.html")
    text = open(kat, encoding="utf-8").read()
    text = replace_block(text, "espa", accordion("espa", CD.ESPA_CATEGORIES, espa))
    text = replace_block(text, "hidrostal", accordion("hidrostal", CD.HIDROSTAL_CATEGORIES, hidro))
    open(kat, "w", encoding="utf-8").write(text)
    json.dump([{k: v for k, v in p.items() if k != "curves"} | {"curve_models": list(p["curves"])} for p in allp],
              open(os.path.join(ROOT, "data", "catalog.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"ESPA: {len(espa)} · Hidrostal: {len(hidro)} · страниц: {len(allp)}")


if __name__ == "__main__":
    main()
