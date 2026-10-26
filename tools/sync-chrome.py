#!/usr/bin/env python3
"""Копирует общие блоки из index.html во все остальные *.html в корне.

Блоки размечены в index.html комментариями:
  <!-- chrome:head -->   ... <!-- /chrome:head -->    шрифты, Tailwind, CSS
  <!-- chrome:top -->    ... <!-- /chrome:top -->     спрайт иконок, шапка, мобильное меню
  <!-- chrome:footer --> ... <!-- /chrome:footer -->  футер
  <!-- chrome:bottom --> ... <!-- /chrome:bottom -->  кнопка «Наверх», скрипты

Запуск после любой правки шапки/футера в index.html:
  python3 tools/sync-chrome.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
BLOCKS = ["head", "top", "footer", "bottom"]


def block_re(name):
    return re.compile(r"<!-- chrome:%s -->(.*?)<!-- /chrome:%s -->" % (name, name), re.S)


def main():
    src = open(SRC, encoding="utf-8").read()
    parts = {}
    for b in BLOCKS:
        m = block_re(b).search(src)
        if not m:
            sys.exit("index.html: нет блока chrome:%s" % b)
        parts[b] = m.group(1)

    for path in sorted(glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "product", "*.html"))):
        if os.path.abspath(path) == os.path.abspath(SRC):
            continue
        text = open(path, encoding="utf-8").read()
        orig = text
        for b in BLOCKS:
            if not block_re(b).search(text):
                print("%s: нет блока chrome:%s — пропуск" % (os.path.basename(path), b))
                continue
            text = block_re(b).sub(
                lambda m, b=b: "<!-- chrome:%s -->%s<!-- /chrome:%s -->" % (b, parts[b], b), text
            )
        if text != orig:
            open(path, "w", encoding="utf-8").write(text)
            print("обновлён", os.path.basename(path))
        else:
            print("без изменений", os.path.basename(path))


if __name__ == "__main__":
    main()
