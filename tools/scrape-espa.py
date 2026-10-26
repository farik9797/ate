#!/usr/bin/env python3
"""Собирает технические данные серий ESPA с официального сайта espa.com (раздел UK).

По каждой серии: название, подзаголовок, описание, особенности (электрика, материалы,
конструкция, ограничения), таблица моделей (электрические данные), диапазоны давления,
кривые Q–H (м³/ч, м), документы (инструкция, каталог, деталировка), главное фото.

Запуск (нужны beautifulsoup4 и lxml):
  python3 tools/scrape-espa.py            -> data/espa-raw.json + assets/img/products/espa/*.jpg
"""
import json
import os
import re
import sys
import time
import urllib.request

from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://www.espa.com"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"

CATEGORIES = [
    ("groundwater-submersible-pumps", "skvazhinnye"),
    ("groundwater-submersible-wet-ends-and-motors", "skvazhinnye-chasti"),
    ("supply-horizontal-surface-pumps", "gorizontalnye"),
    ("supply-vertical-surface-pumps", "vertikalnye"),
    ("supply-booster-pumps-and-sets", "stancii"),
    ("supply-control-and-automation-devices", "avtomatika"),
    ("recirculation-and-filtration-swimming-pool-pumps", "basseyny"),
    ("evacuation-drainage-pumps-and-sets", "drenazh"),
]
CAT_SLUGS = {c for c, _ in CATEGORIES} | {
    "recirculation-and-filtration-filtration-sets-for-swimming-pools",
    "recirculation-and-filtration-cleaning-swimming-pool-pumps",
    "recirculation-and-filtration-counter-current-pumps",
    "recirculation-and-filtration-whirlpool-and-spa-pumps",
    "recirculation-and-filtration-pumps-for-other-applications",
}


def get(url, xhr=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **({"X-Requested-With": "XMLHttpRequest"} if xhr else {})})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception as e:  # noqa: BLE001
            if attempt == 2:
                raise
            time.sleep(2)
    return ""


def clean(t):
    return re.sub(r"\s+", " ", t or "").strip()


def soup(html):
    return BeautifulSoup(html, "lxml")


def category_products(cat):
    s = soup(get(f"{BASE}/uk/{cat}/"))
    main = s.find("main") or s.body
    seen, out = set(), []
    for a in main.find_all("a", href=True):
        h = a["href"]
        m = re.fullmatch(r"/uk/([a-z0-9-]+)/", h)
        if not m or m.group(1) in CAT_SLUGS or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        out.append(m.group(1))
    return out


def parse_info(slug):
    s = soup(get(f"{BASE}/uk/{slug}/"))
    main = s.find("main") or s.body
    name = clean((main.find("h1") or {}).get_text() if main.find("h1") else slug)
    img = main.select_one(".passi-producte-item img")
    sub = main.select_one("p.text-ml")
    desc = [clean(p.get_text()) for p in main.select("div.bloc > div.text p") if clean(p.get_text())]
    groups = []
    for blk in main.select("div.bloc-minim"):
        title = blk.select_one("div.text-bold p")
        ul = blk.find("ul", class_="chevron-list")
        if not title or not ul:
            continue
        items = []
        for li in ul.find_all("li"):
            b = li.find("b")
            key = clean(b.get_text()).rstrip(":") if b else ""
            val = clean(li.get_text())
            if b:
                val = clean(val[len(clean(b.get_text())):])
            items.append([key, val])
        groups.append({"title": clean(title.get_text()), "items": items})
    return {
        "name": name,
        "image": img["src"] if img else "",
        "subtitle": clean(sub.get_text()) if sub else "",
        "description": desc,
        "features": groups,
    }


def parse_specs(slug):
    html = get(f"{BASE}/uk/{slug}/?especificaciones")
    s = soup(html)
    serie = s.find("input", attrs={"name": "serie"})
    tables = []
    tooltips = {}
    for t in s.find_all("table"):
        head_rows = t.find("thead").find_all("tr") if t.find("thead") else []
        heads = [[clean(th.get_text()) + ("|" + th.get("colspan") if th.get("colspan") else "") for th in r.find_all("th")] for r in head_rows]
        rows = []
        for tr in (t.find("tbody") or t).find_all("tr"):
            cells = []
            for td in tr.find_all("td"):
                tip = td.select_one(".model-tooltip")
                if tip:
                    content = tip.select_one(".model-tooltip-content")
                    model = clean(tip.get_text().replace(content.get_text(), "") if content else tip.get_text())
                    if content:
                        lims = {}
                        for li in content.find_all("li"):
                            k, _, v = clean(li.get_text()).partition(":")
                            lims[k.strip()] = v.strip()
                        tooltips[model] = lims
                    cells.append(model)
                else:
                    cells.append(clean(td.get_text()))
            if cells:
                rows.append(cells)
        title_el = t.find_previous(["h3", "h2"])
        tables.append({"title": clean(title_el.get_text()) if title_el else "", "head": heads, "rows": rows})
    return {"serie": serie["value"] if serie else None, "tables": tables, "models": tooltips}


def parse_curves(serie):
    if not serie:
        return {}
    url = (f"{BASE}/uk/model/grafica?grafica=pressio&serie={serie}&sep_mil=.&sep_dec=%2C"
           "&frequencia=50&cabal=7&pressio=2&potencia=14&npsh=4")
    try:
        data = json.loads(get(url, xhr=True))
    except Exception:  # noqa: BLE001
        return {}
    curves = {}
    for ser in data.get("series", []):
        pts = []
        for p in ser.get("data", []):
            x, y = (p["x"], p["y"]) if isinstance(p, dict) else (p[0], p[1])
            pts.append([round(float(x), 3), round(float(y), 2)])
        curves.setdefault(ser.get("name", "?"), []).extend(pts)
    for k in curves:
        curves[k] = sorted({tuple(p) for p in curves[k]})
        curves[k] = [list(p) for p in curves[k]]
    return curves


def parse_docs(slug):
    s = soup(get(f"{BASE}/uk/{slug}/?recursos"))
    out = []
    for a in s.find_all("a", href=True):
        h = a["href"]
        if "/download/docs/" in h:
            out.append(h)
    return list(dict.fromkeys(out))


def main():
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    imgdir = os.path.join(ROOT, "assets", "img", "products", "espa")
    os.makedirs(imgdir, exist_ok=True)
    result = []
    for cat, cat_key in CATEGORIES:
        slugs = category_products(cat)
        print(f"{cat}: {len(slugs)}", file=sys.stderr)
        for slug in slugs:
            info = parse_info(slug)
            specs = parse_specs(slug)
            curves = parse_curves(specs["serie"])
            docs = parse_docs(slug)
            img_local = ""
            if info["image"]:
                img_local = f"assets/img/products/espa/{slug}.jpg"
                dest = os.path.join(ROOT, img_local)
                if not os.path.exists(dest):
                    req = urllib.request.Request(info["image"], headers={"User-Agent": UA})
                    with urllib.request.urlopen(req, timeout=40) as r, open(dest, "wb") as f:
                        f.write(r.read())
            result.append({"slug": slug, "category": cat_key, "source": f"{BASE}/uk/{slug}/", **info,
                           "image_local": img_local, **specs, "curves": curves, "docs": docs})
            print(f"  {slug}: models={len(specs['models'])} curves={len(curves)} docs={len(docs)}", file=sys.stderr)
            time.sleep(0.3)
    with open(os.path.join(ROOT, "data", "espa-raw.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(f"saved {len(result)} series", file=sys.stderr)


if __name__ == "__main__":
    main()
