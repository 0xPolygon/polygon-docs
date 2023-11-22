#!/usr/bin/env bash
set -euo pipefail

/Library/Frameworks/Python.framework/Versions/3.11/bin/pip3/virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
mkdocs serve --strict

