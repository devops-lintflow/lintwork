#!/bin/bash

pip install -U pywin32
pip install -U pyinstaller
pip install -Ur requirements.txt

pyinstaller --clean --name lintaosp --upx-dir /usr/bin -F aosp.py
