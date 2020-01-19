#!/usr/bin/env bash

if [[ ! -d 'venv' ]]; then
  echo "Create virtual environment"
  python3 -m venv venv --prompt sPYder
fi

source venv/bin/activate

if [[ -f requirements.txt ]]; then
  echo "Install requirements"
  pip install -r requirements.txt
fi

if [[ -f requirements.dev.txt ]] && [[ $1 != 'production' ]]; then
  echo "Install dev requirements"
  pip install -r requirements.dev.txt
fi

