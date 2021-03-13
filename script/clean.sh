#!/bin/bash

chmod 644 .gitignore .pre-commit-config.yml .travis.yml
chmod 644 LICENSE Makefile MANIFEST.in README.md requirements.txt setup.cfg tox.ini
chmod 644 work.py setup.py

find lintwork tests -name "*.py" -exec chmod 644 {} \;
find lintwork tests -name "*.yml" -exec chmod 644 {} \;
find . -name "*.pyc" ! -path "*.venv*" -exec rm -rf {} \;
find . -name "*.sh" ! -path "*.venv*" -exec chmod 755 {} \;
find . -name "__pycache__" ! -path "*.venv*" -exec rm -rf {} \;
