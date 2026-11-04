#!/usr/bin/env python3
"""Notify IndexNow (Bing, Copilot, Yandex, ...) about pages that changed in a deploy.

  indexnow.py snapshot <file>         save lastmod of all URLs from the live sitemaps
  indexnow.py notify <file> <public>  compare with the new build and submit new/changed URLs

Never fails the deploy: errors are printed and the script exits 0.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

HOST = "seatable.com"
KEY = "1d7827f9766f0d44cd25fa5316aaf1c3"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
LANGS = ["en", "de", "fr", "es", "pt", "ru"]
GROUPS = ["page", "post", "help", "template", "lifestyle"]
MAX_URLS = 10000  # IndexNow limit per request

ENTRY = re.compile(r"<loc>(.*?)</loc>\s*(?:<lastmod>(.*?)</lastmod>)?", re.S)


def parse(xml):
    return {loc: lastmod or "" for loc, lastmod in ENTRY.findall(xml)}


def snapshot(out):
    urls = {}
    for lang in LANGS:
        for group in GROUPS:
            url = f"https://{HOST}/{lang}/{group}-sitemap.xml"
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    urls.update(parse(r.read().decode()))
            except Exception as e:  # e.g. a sitemap that does not exist yet
                print(f"skip {url}: {e}")
    Path(out).write_text(json.dumps(urls))
    print(f"snapshot: {len(urls)} URLs")


def notify(snapshot_file, public):
    old = json.loads(Path(snapshot_file).read_text())
    if not old:
        print("empty snapshot, nothing submitted (would otherwise send every URL)")
        return
    new = {}
    for f in Path(public).glob("*/*-sitemap.xml"):
        new.update(parse(f.read_text()))
    changed = sorted(u for u, lastmod in new.items() if old.get(u) != lastmod)
    print(f"{len(changed)} new or changed URLs")
    if not changed:
        return
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": KEY_LOCATION, "urlList": changed[:MAX_URLS]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow response: {r.status}")
    for u in changed[:20]:
        print("  " + u)


if __name__ == "__main__":
    try:
        if sys.argv[1] == "snapshot":
            snapshot(sys.argv[2])
        elif sys.argv[1] == "notify":
            notify(sys.argv[2], sys.argv[3])
    except Exception as e:
        print(f"IndexNow skipped: {e}")
