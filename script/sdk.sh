#!/bin/bash

TAG=6858069_latest
NAME=commandlinetools-linux-$TAG

curl -L https://dl.google.com/android/repository/$NAME.zip -o $NAME.zip
unzip $NAME

# List check
#./cmdline-tools/bin/lint --list
#./cmdline-tools/bin/lint --show

# Run check
#CHECK="Correctness,Correctness:Messages,Security,Compliance,Performance,Performance:Application Size,Usability:Typography,Usability:Icons,Usability,Productivity,Accessibility,Internationalization,Internationalization:Bidirectional Text"
#PROJECT="/path/to/project"
#find $PROJECT -type f -name "build.gradle" -exec rm -f {} \;
#./cmdline-tools/bin/lint --check "$CHECK" --disable "LintError" --nolines --quiet $PROJECT
