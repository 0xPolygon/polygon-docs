#!/usr/bin/env bash
set -euo pipefail

virtualenv venv
source venv/bin/activate
mkdocs serve --strict