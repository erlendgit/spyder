#!/usr/bin/env bash

if [[ ! -d '_bin/venv' ]]; then
  echo "Create virtual environment"
  python3 -m venv _bin/venv --prompt sPYder
fi

source _bin/venv/bin/activate

if [[ -f requirements.txt ]]; then
  echo "Install requirements"
  pip install -r _project/requirements.txt
fi
