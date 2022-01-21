FROM craftslab/androiddocker:latest

USER root
RUN apt update && \
    apt install -y bzip2 iptables libgomp1 libpopt0 libxml2-dev libxslt1-dev pandoc upx xz-utils zlib1g && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN ln -s /usr/bin/pip3 /usr/bin/pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    python -m pip install -U pip
RUN curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/containerd.io_1.4.6-1_amd64.deb && \
    curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-ce-cli_20.10.7~3-0~ubuntu-focal_amd64.deb && \
    curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-ce-rootless-extras_20.10.7~3-0~ubuntu-focal_amd64.deb && \
    curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-ce_20.10.7~3-0~ubuntu-focal_amd64.deb && \
    curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-scan-plugin_0.8.0~ubuntu-focal_amd64.deb && \
    dpkg -i *.deb && \
    rm *.deb
RUN usermod -a -G docker craftslab

USER craftslab
WORKDIR /home/craftslab
ENV PATH /home/craftslab/.local/bin:$PATH
ENV PATH /home/craftslab/opt/checkstyle/lib:$PATH
ENV PATH /home/craftslab/opt/go/bin:$PATH
ENV PATH /home/craftslab/opt/groovylint:$PATH
ENV PATH /home/craftslab/opt/spotbugs/bin:$PATH
ENV PATH /home/craftslab/opt/scancode:$PATH
RUN mkdir -p ~/.local/bin
RUN pip install cpplint
RUN curl -L https://go.dev/dl/go1.17.6.linux-amd64.tar.gz -o go.tar.gz && \
    tar zxvf go.tar.gz && \
    sudo mv go ~/opt/ && \
    rm -rf go.tar.gz
RUN curl -L https://github.com/golangci/golangci-lint/releases/download/v1.38.0/golangci-lint-1.38.0-linux-amd64.deb -o golangci-lint.deb && \
    sudo dpkg -i golangci-lint.deb && \
    rm golangci-lint.deb
RUN curl -L https://github.com/Ableton/groovylint/archive/0.9.1.tar.gz -o groovylint.tar.gz && \
    tar zxvf groovylint.tar.gz && \
    mv groovylint-0.9.1 ~/opt/groovylint && \
    cd ~/opt/groovylint && \
    pip install -Ur requirements.txt && \
    python fetch_jars.py --codenarc 2.0.0 --gmetrics 1.1 --slf4j 1.7.30 --output-dir ./resources && \
    cd - && \
    rm -rf groovylint.tar.gz
RUN curl -L https://github.com/checkstyle/checkstyle/releases/download/checkstyle-8.41/checkstyle-8.41-all.jar -o checkstyle.jar && \
    curl -L https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml -o google_checks.xml && \
    mkdir -p ~/opt/checkstyle/{etc,lib} && \
    mv google_checks.xml ~/opt/checkstyle/etc/ && \
    mv checkstyle.jar ~/opt/checkstyle/lib/
RUN curl -L https://github.com/spotbugs/spotbugs/releases/download/4.2.2/spotbugs-4.2.2.tgz -o spotbugs.tgz && \
    tar zxvf spotbugs.tgz && \
    mv spotbugs-4.2.2 ~/opt/spotbugs && \
    chmod +x ~/opt/spotbugs/bin/* && \
    rm -rf spotbugs.tgz
RUN curl -LO https://raw.githubusercontent.com/torvalds/linux/master/scripts/checkpatch.pl && \
    curl -LO https://raw.githubusercontent.com/torvalds/linux/master/scripts/const_structs.checkpatch && \
    curl -LO https://raw.githubusercontent.com/torvalds/linux/master/scripts/spelling.txt && \
    chmod +x checkpatch.pl && \
    mv checkpatch.pl ~/.local/bin/ && \
    chmod -x const_structs.checkpatch && \
    mv const_structs.checkpatch ~/.local/bin/ && \
    chmod -x spelling.txt && \
    mv spelling.txt ~/.local/bin/
RUN pip install flake8
RUN curl -L https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init -o rustup-init && \
    chmod +x rustup-init && \
    ./rustup-init --default-host x86_64-unknown-linux-gnu --default-toolchain stable --profile default -y && \
    source ~/.cargo/env && \
    rustup update && \
    rustup component add clippy && \
    rm -f rustup-init
RUN curl -L https://github.com/koalaman/shellcheck/releases/download/v0.7.1/shellcheck-v0.7.1.linux.x86_64.tar.xz -o shellcheck.tar.xz && \
    tar Jxvf shellcheck.tar.xz && \
    chmod +x shellcheck-v0.7.1/shellcheck && \
    mv shellcheck-v0.7.1/shellcheck ~/.local/bin/ && \
    rm -rf shellcheck*
RUN curl -LO https://github.com/nexB/scancode-toolkit/archive/refs/tags/v21.6.7.zip && \
    unzip v21.6.7.zip && \
    rm -f v21.6.7.zip && \
    mv scancode-toolkit-21.6.7 ~/opt/scancode && \
    cd ~/opt/scancode && \
    ./scancode --reindex-licenses
RUN curl -L https://github.com/mrtazz/checkmake/archive/refs/tags/0.2.0.tar.gz -o checkmake.tar.gz && \
    tar zxvf checkmake.tar.gz && \
    pushd checkmake-0.2.0 && \
    export BUILDER_NAME="name" && \
    export BUILDER_EMAIL="name@example.com" && \
    go env -w GOPROXY=https://goproxy.cn,direct && \
    sed -i "s/^VERSION :=.*$/VERSION := 0.2.0/g" Makefile && \
    make clean all test && \
    chmod +x checkmake && \
    mv checkmake ~/.local/bin/ && \
    popd && \
    rm -rf checkmake*
RUN mkdir src
COPY . src
RUN cd src; make install; cd .. && \
    cp src/dist/* . && \
    cp src/lintwork/config/*.yml . && \
    sudo rm -rf src
