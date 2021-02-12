# lintaosp

[![Actions Status](https://github.com/craftslab/lintaosp/workflows/CI/badge.svg?branch=master&event=push)](https://github.com/craftslab/lintaosp/actions?query=workflow%3ACI)
[![Docker](https://img.shields.io/docker/pulls/craftslab/lintaosp)](https://hub.docker.com/r/craftslab/lintaosp)
[![License](https://img.shields.io/github/license/craftslab/lintaosp.svg?color=brightgreen)](https://github.com/craftslab/lintaosp/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/lintaosp.svg?color=brightgreen)](https://pypi.org/project/lintaosp)
[![Tag](https://img.shields.io/github/tag/craftslab/lintaosp.svg?color=brightgreen)](https://github.com/craftslab/lintaosp/tags)



## Introduction

*lintaosp* is a lint worker of *[lintflow](https://github.com/craftslab/lintflow/)* on AOSP written in Python.



## Prerequisites

- Python >= 3.7



## Run

- **Local mode**

```bash
git clone https://github.com/craftslab/lintaosp.git

cd lintaosp
pip install -Ur requirements.txt
python aosp.py --config-file="config.yml" --input-text="{base64}" --output-file="output.json"
```



- **Service mode**

```bash
git clone https://github.com/craftslab/lintaosp.git

cd lintaosp
pip install -Ur requirements.txt
python aosp.py --config-file="config.yml" --listen-url="127.0.0.1:9090"
```



## Docker

- **Local mode**

```bash
git clone https://github.com/craftslab/lintaosp.git

cd lintaosp
docker build --no-cache -f Dockerfile -t craftslab/lintaosp:latest .
docker run -it -v /tmp:/tmp craftslab/lintaosp:latest ./lintaosp --config-file="config.yml" --input-text="{base64}" --output-file="/tmp/output.json"
```



- **Service mode**

```bash
git clone https://github.com/craftslab/lintaosp.git

cd lintaosp
docker build --no-cache -f Dockerfile -t craftslab/lintaosp:latest .
docker run -it -p 9090:9090 craftslab/lintaosp:latest ./lintaosp --config-file="config.yml" --listen-url="127.0.0.1:9090"
```



## Usage

```
usage: aosp.py [-h] --config-file CONFIG_FILE
               [--input-text INPUT_TEXT | --listen-url LISTEN_URL]
               [--output-file OUTPUT_FILE] [-v]

Lint AOSP

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        config file (.yml)
  --input-text INPUT_TEXT
                        input text (base64)
  --listen-url LISTEN_URL
                        listen url (host:port)
  --output-file OUTPUT_FILE
                        output file (.json|.txt|.xlsx)
  -v, --version         show program's version number and exit
```



## Settings

*lintaosp* parameters can be set in the directory [config](https://github.com/craftslab/lintaosp/blob/master/lintaosp/config).

An example of configuration in [config.yml](https://github.com/craftslab/lintaosp/blob/master/lintaosp/config/config.yml):

```yaml
apiVersion: v1
kind: worker
metadata:
  name: lintaosp
spec:
  - strings
```



## Design

![design](design.png)



## Errorformat

- **Error type**

```
E: Error
I: Information
W: Warning
```

- **JSON format**

```json
{
  "fileName": "/path/to/file",
  "lineNum": 1,
  "colNum": 1,
  "errorNum": "strings",
  "errorDetails": "details",
  "errorType": "E"
}
```

- **Text format**

```text
{fileName}:{lineNum}:{colNum}:{errorNum}:{errorDetails}:{errorType}
```



## License

Project License can be found [here](LICENSE).



## Reference

- [errorformat](https://github.com/reviewdog/errorformat)
- [gRPC](https://grpc.io/docs/languages/python/)
- [protocol-buffers](https://developers.google.com/protocol-buffers/docs/proto3)
