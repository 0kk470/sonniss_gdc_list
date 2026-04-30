#!/usr/bin/env python3
"""
GDC Sonniss 音效包结构提取工具
用法: python generate_catalog.py
输出: 打印各 ZIP 内的顶层目录列表，供 AI 分析后生成 catalog.md。
"""

import zipfile
import os
import re
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def parse_zip_name(filename):
    m = re.search(r"GDC\s*-\s*(\d{4})_(\d+)", filename, re.IGNORECASE)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def get_top_dirs(zip_path):
    with zipfile.ZipFile(zip_path) as zf:
        return sorted(set(
            e.split("/")[0] for e in zf.namelist()
            if "/" in e and not e.startswith("__MACOSX")
        ))


if __name__ == "__main__":
    by_year = defaultdict(dict)
    for f in sorted(os.listdir(BASE_DIR)):
        if f.lower().endswith(".zip"):
            year, part = parse_zip_name(f)
            if year:
                by_year[year][part] = os.path.join(BASE_DIR, f)

    for year in sorted(by_year):
        for part in sorted(by_year[year]):
            print(f"\n=== {year} / Part {part} ===")
            for d in get_top_dirs(by_year[year][part]):
                print(f"  {d}")
