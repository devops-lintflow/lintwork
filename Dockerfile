FROM craftslab/androiddocker:android-30

USER root
RUN apt update && \
    apt install -y upx
RUN ln -s /usr/bin/pip3 /usr/bin/pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    python -m pip install -U pip

USER craftslab
WORKDIR /home/craftslab
ENV PATH /home/craftslab/.local/bin:/usr/lib/dart/bin:$PATH
RUN python -m pip install flake8
RUN curl -LO https://raw.githubusercontent.com/torvalds/linux/master/scripts/checkpatch.pl && \
    chmod +x checkpatch.pl && \
    mv checkpatch.pl ~/.local/bin/
RUN curl -LO https://raw.githubusercontent.com/google/styleguide/gh-pages/cpplint/cpplint.py && \
    chmod +x cpplint.py && \
    mv cpplint.py ~/.local/bin/
RUN curl -L https://storage.googleapis.com/dart-archive/channels/stable/release/latest/linux_packages/dart_2.12.1-1_amd64.deb -o dart.deb && \
    sudo dpkg -i dart.deb && \
    rm dart.deb
RUN curl -L https://github.com/golangci/golangci-lint/releases/download/v1.38.0/golangci-lint-1.38.0-linux-amd64.deb -o golangci-lint.deb && \
    sudo dpkg -i golangci-lint.deb && \
    rm golangci-lint.deb
RUN curl -L https://github.com/checkstyle/checkstyle/releases/download/checkstyle-8.41/checkstyle-8.41-all.jar -o checkstyle.jar && \
    mkdir ~/opt/checkstyle && \
    mv checkstyle.jar ~/opt/checkstyle/
RUN curl -L https://github.com/koalaman/shellcheck/releases/download/v0.7.1/shellcheck-v0.7.1.linux.x86_64.tar.xz -o shellcheck.tar.xz && \
    tar Jxvf shellcheck.tar.xz && \
    chmod +x shellcheck-v0.7.1/shellcheck && \
    mv shellcheck-v0.7.1/shellcheck ~/.local/bin/ && \
    rm -rf shellcheck*
RUN curl -L https://github.com/Ableton/groovylint/archive/0.9.1.tar.gz -o groovylint.tar.gz && \
    tar zxvf groovylint.tar.gz && \
    mv groovylint-0.9.1 ~/opt/groovylint && \
    cd ~/opt/groovylint && \
    pip install -Ur requirements.txt && \
    python fetch_jars.py --codenarc 2.0.0 --gmetrics 1.1 --slf4j 1.7.30 --output-dir ./resources && \
    cd - && \
    rm -rf groovylint.tar.gz
RUN mkdir src
COPY . src
RUN cd src; make install; cd .. && \
    cp src/dist/* . && \
    cp src/lintwork/config/*.yml . && \
    sudo rm -rf src
