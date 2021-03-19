#!/bin/bash

list="$(find tests/* -maxdepth 0 -type d | grep -v __pycache__)"
coverage run --source=lintwork,tests -m pytest -v --capture=no $list
