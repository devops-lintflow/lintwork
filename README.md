# lintwork

[![Actions Status](https://github.com/devops-lintflow/lintwork/workflows/ci/badge.svg?branch=main&event=push)](https://github.com/devops-lintflow/lintwork/actions?query=workflow%3Aci)
[![License](https://img.shields.io/github/license/devops-lintflow/lintwork.svg?color=brightgreen)](https://github.com/devops-lintflow/lintwork/blob/main/LICENSE)
[![Tag](https://img.shields.io/github/tag/devops-lintflow/lintwork.svg?color=brightgreen)](https://github.com/devops-lintflow/lintwork/tags)



## Introduction

*lintwork* is a lint worker of *[lintflow](https://github.com/devops-lintflow/lintflow/)* written in Python.



## Prerequisites

- gRPC >= 1.36.0
- Python >= 3.7.0



## Run

- **Local mode**

```bash
pip install -Ur requirements.txt
python work.py --config-file="tests/data/config.yml" --lint-name="lintshell" --lint-project="tests/data/project" --output-file="output.json"
```



- **Service mode**

```bash
pip install -Ur requirements.txt
python work.py --config-file="tests/data/config.yml" --listen-url="127.0.0.1:9090"
```



## Docker

- **Local mode**

```bash
docker build --no-cache -f Dockerfile -t craftslab/lintwork:latest .
docker run -it -v tests/data:/tmp craftslab/lintwork:latest ./lintwork --config-file="/tmp/config.yml" --lint-name="lintshell" --lint-project="/tmp/project" --output-file="/tmp/output.json"
```



- **Service mode**

```bash
docker build --no-cache -f Dockerfile -t craftslab/lintwork:latest .
docker run -it --network=host craftslab/lintwork:latest ./lintwork --config-file="config.yml" --listen-url="127.0.0.1:9090"
```



## Usage

```
usage: work.py [-h] --config-file CONFIG_FILE [--lint-project LINT_PROJECT | --listen-url LISTEN_URL]
               [--lint-name LINT_NAME] [--output-file OUTPUT_FILE] [-v]

Lint Work

options:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        config file (.yml)
  --lint-project LINT_PROJECT
                        lint project (e.g., tests/data/project)
  --listen-url LISTEN_URL
                        listen url (host:port)
  --lint-name LINT_NAME
                        lint name (e.g., lintshell)
  --output-file OUTPUT_FILE
                        output file (.json|.txt|.xlsx)
  -v, --version         show program's version number and exit
```



## Settings

*lintwork* parameters can be set in the directory [config](https://github.com/devops-lintflow/lintwork/blob/main/lintwork/config).

An example of configuration in [config.yml](https://github.com/devops-lintflow/lintwork/blob/main/lintwork/config/config.yml):

```yaml
apiVersion: v1
kind: worker
metadata:
  name: lintwork
spec:
  lintai:
    lintgpt:
  lintcommit:
    contentcheck:
    messagecheck:
  lintcpp:
    cpplint:
  lintjava:
    aosplint:
      - --disable
      - LintError
      - --nolines
      - --quiet
    checkstyle:
      - -jar
      - /home/craftslab/opt/checkstyle/lib/checkstyle.jar
      - -c=/home/craftslab/opt/checkstyle/etc/google_checks.xml
    javalint:
      - -jar
      - /home/craftslab/opt/javalint/lib/javalint.jar
      - --file
    stringscheck:
  lintkernel:
    checkpatch:
      - --no-summary
      - --no-tree
      - --terse
  lintmake:
    checkmake:
      - --format=:{{.LineNumber}}::{{.Violation}}\n
  lintpython:
    flake8:
  lintshell:
    shellcheck:
      - --format=gcc
```



## Project

- **Commit Files**

```
lintwork-20240630231055/
├── COMMIT_MSG
├── {change-number}-{commit-id}.meta
├── {change-number}-{commit-id}.patch
└── path/to/file
```

- **Commit Meta**

```json
{
  "branch": "main",
  "owner": "name",
  "project": "name",
  "revision": "39fe82c424a319e9613126d2ef1c837e114440c5",
  "updated": "2024-09-20 07:15:44.639000000",
  "url": "http://127.0.0.1:8080"
}
```



## Report

- **JSON**

```json
{
  "lint": [
    {
      "file": "name",
      "line": 1,
      "type": "Error",
      "details": "text"
    }
  ]
}
```

- **Text**

```text
{lint}:{file}:{line}:{type}:{details}
```



## License

Project License can be found [here](LICENSE).



## Reference

### Linter

- [android-lint](https://developer.android.com/studio/write/lint)
- [checkmake](https://github.com/mrtazz/checkmake)
- [checkpatch](https://github.com/torvalds/linux/blob/master/scripts/checkpatch.pl)
- [checkstyle](https://checkstyle.org/)
- [cpplint](https://github.com/cpplint/cpplint)
- [flake8](https://flake8.pycqa.org/)
- [golangci-lint](https://golangci-lint.run/)
- [groovylint](https://github.com/Ableton/groovylint)
- [rust-clippy](https://rust-lang.github.io/rust-clippy/)
- [shellcheck](https://www.shellcheck.net/)
- [spotbugs](https://spotbugs.github.io/)



### Misc

- [errorformat](https://github.com/reviewdog/errorformat)
- [gRPC](https://grpc.io/docs/languages/python/)
- [protocol-buffers](https://developers.google.com/protocol-buffers/docs/proto3)
- [reviewdog](https://github.com/reviewdog/reviewdog)
