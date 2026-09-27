#!/bin/sh
# Local wrapper. Does not download or execute remote code.
set -eu
cd "$(dirname "$0")/.."
exec python3 scripts/install.py "$@"
