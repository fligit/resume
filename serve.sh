#!/usr/bin/env bash
# Serve the deck locally. Required because index.html loads slides via fetch(),
# which browsers block on file:// URLs.
set -e
cd "$(dirname "$0")"
PORT="${1:-8000}"
echo "Serving on http://localhost:${PORT}"
python3 -m http.server "$PORT"
