#!/usr/bin/env bash
set -euo pipefail

/Users/ammatlala/Library/Python/3.11/bin/virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
mkdocs serve

