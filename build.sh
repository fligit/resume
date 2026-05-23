#!/usr/bin/env bash
# Bundle slides/*.html into a single dist/index.html that works on file://
# (no fetch, no local server needed).
set -e
cd "$(dirname "$0")"

mkdir -p dist
python3 build.py
echo "✓ Built dist/index.html — double-click to open."
