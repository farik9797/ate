#!/usr/bin/env python3
"""Обложки категорий каталога: вырезает фон у фото серий и собирает 1–3 насоса в одну картинку.

Вход:  assets/img/products/<brand>/*.jpg (фото с сайтов производителей, однотонный фон).
Выход: assets/img/cats/<brand>-<категория>.webp — прозрачный фон, 720×540.

Запуск (нужен Pillow):  python3 tools/build-covers.py
"""
import os

from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "cats")
W, H = 720, 540

# категория -> фото (первое — главное, по центру и крупнее)
COVERS = {
    "espa-skvazhinnye": ["espa/acuaria-37", "espa/acuaria-57", "espa/acuaria-07s"],
    "espa-skvazhinnye-chasti": ["espa/es4-04", "espa/motor-4wm-pm-4-"],
    "espa-gorizontalnye": ["espa/aspri-35n", "espa/tecno-25"],
    "espa-vertikalnye": ["espa/multi-vs-15", "espa/ve-121n"],
    "espa-stancii": ["espa/cke-3", "espa/tecnopres-25"],
    "espa-avtomatika": ["espa/cimm-vessels", "espa/speedrive-v2", "espa/pressdrive"],
    "espa-basseyny": ["espa/silen-s2", "espa/silen-i"],
    "espa-drenazh": ["espa/drainex-400", "espa/vigila", "espa/vigicor"],
    "hidrostal-centrobezhnye": ["hidrostal/submersible", "hidrostal/end-suction"],
    "hidrostal-osevye": ["hidrostal/axial-column", "hidrostal/vertical-turbine"],
    "hidrostal-sistemy": ["hidrostal/prerostal", "hidrostal/preroclean"],
}
KEY = (255, 0, 255)


def cutout(path, tol_white=34):
    """Убирает фон, связанный с краями кадра (белый или чёрный), и обрезает по содержимому."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    corners = [im.getpixel(p) for p in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1))]
    dark = sum(sum(c) for c in corners) / 12 < 60
    tol = 18 if dark else tol_white
    work = im.copy()
    seeds = [(x, y) for x in range(0, w, 6) for y in (0, h - 1)] + [(x, y) for y in range(0, h, 6) for x in (0, w - 1)]
    for s in seeds:
        px = work.getpixel(s)
        if px == KEY:
            continue
        if (sum(px) < 3 * 70) if dark else (min(px) > 200):
            ImageDraw.floodfill(work, s, KEY, thresh=tol)
    mask = Image.new("L", (w, h), 255)
    mpx, wpx = mask.load(), work.load()
    for y in range(h):
        for x in range(w):
            if wpx[x, y] == KEY:
                mpx[x, y] = 0
    mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    rgba = im.convert("RGBA")
    rgba.putalpha(mask)
    return rgba.crop(mask.point(lambda v: 255 if v > 24 else 0).getbbox())


def compose(parts):
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    rel = [1.0, 0.8, 0.7][: len(parts)]
    scale = 1.0
    while True:  # подбираем масштаб, чтобы композиция влезла по ширине с перекрытием 18%
        sized = []
        for p, r in zip(parts, rel):
            k = min(H * 0.96 * r * scale / p.height, W * 0.72 * scale / p.width)
            sized.append(p.resize((max(1, int(p.width * k)), max(1, int(p.height * k))), Image.LANCZOS))
        total = sized[0].width + sum(s.width * 0.82 for s in sized[1:])
        if total <= W * 0.98 or scale < 0.3:
            break
        scale *= 0.94
    main = sized[0]
    mx = (W - main.width) // 2 + (int(sized[1].width * 0.18) if len(sized) == 2 else 0)
    if len(sized) >= 2:
        s = sized[1]
        x = max(0, mx - int(s.width * 0.82))
        canvas.alpha_composite(s, (x, H - s.height))
    if len(sized) == 3:
        s = sized[2]
        x = min(W - s.width, mx + main.width - int(s.width * 0.18))
        canvas.alpha_composite(s, (x, H - s.height))
    canvas.alpha_composite(main, (mx, H - main.height))
    return canvas.crop(canvas.getbbox())


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, srcs in COVERS.items():
        tol = 96 if name.startswith("hidrostal") else 34  # у фото Hidrostal серые тени на полу
        parts = [cutout(os.path.join(ROOT, "assets", "img", "products", s + ".jpg"), tol) for s in srcs]
        img = compose(parts)
        img.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=86, method=6)
        print(name, img.size)


if __name__ == "__main__":
    main()
