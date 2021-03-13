#!/bin/bash

# Install AOSP SDK
#
# Example 1
# ./cmdline-tools/bin/lint --list
# ./cmdline-tools/bin/lint --show
#
# Example 2
# CHECK="Correctness,Correctness:Messages,Security,Compliance,Performance,Performance:Application Size,Usability:Typography,Usability:Icons,Usability,Productivity,Accessibility,Internationalization,Internationalization:Bidirectional Text"
# PROJECT="/path/to/project"
# find $PROJECT -type f -name "build.gradle" -exec rm -f {} \;
# ./cmdline-tools/bin/lint --check "$CHECK" --disable LintError --nolines --quiet $PROJECT
NAME=commandlinetools-linux-6858069_latest
curl -L https://dl.google.com/android/repository/$NAME.zip -o $NAME.zip
unzip $NAME
