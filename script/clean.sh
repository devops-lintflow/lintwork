#!/bin/bash

chmod 644 .gitignore .pre-commit-config.yml .travis.yml
chmod 644 LICENSE Makefile MANIFEST.in README.md requirements.txt setup.cfg tox.ini
chmod 644 aosp.py setup.py

find lintaosp tests -name "*.py" -exec chmod 644 {} \;
find lintaosp tests -name "*.yml" -exec chmod 644 {} \;
find . -name "*.pyc" ! -path "*.venv*" -exec rm -rf {} \;
find . -name "*.sh" ! -path "*.venv*" -exec chmod 755 {} \;
find . -name "__pycache__" ! -path "*.venv*" -exec rm -rf {} \;
