#!/bin/bash

if [ "$1" = "all" ]; then
  coverage run --source=lintwork,tests -m pytest -v --capture=no
else
  list="$(find tests/* -maxdepth 0 -type d | grep -v __pycache__ | grep -v work)"
  coverage run --source=lintwork,tests -m pytest -v --capture=no $list
fi
