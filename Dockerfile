FROM ubuntu:20.04

USER root
ARG DEBIAN_FRONTEND=noninteractive
ARG GID=1000
ARG UID=1000
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV SHELL="/bin/bash"
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update -y > /dev/null && \
    apt install -y bzip2 ca-certificates curl expect ftp git gnupg iptables && \
    apt install -y libgomp1 libpopt0 libxml2-dev libxslt1-dev && \
    apt install -y pandoc psmisc python3 python3-dev python3-pip python3-venv && \
    apt install -y sudo unzip vim xz-utils zip zlib1g
RUN apt autoremove --purge -y > /dev/null && \
    apt autoclean -y > /dev/null && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/log/* && \
    rm -rf /tmp/*
RUN echo "alias pip=pip3" | tee --append /etc/bash.bashrc && \
    echo "alias python=python3" | tee --append /etc/bash.bashrc && \
    echo "StrictHostKeyChecking no" | tee --append /etc/ssh/ssh_config && \
    echo "craftslab ALL=(ALL) NOPASSWD: ALL" | tee --append /etc/sudoers && \
    echo "dash dash/sh boolean false" | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash && \
    groupadd -g $GID craftslab && \
    useradd -d /home/craftslab -ms /bin/bash -g craftslab -u $UID craftslab
RUN pip install -U pyinstaller

USER craftslab
WORKDIR /home/craftslab
ENV PATH=/home/craftslab/.local/bin:$PATH
ENV PATH=/home/craftslab/opt/checkstyle/lib:$PATH
ENV PATH=/home/craftslab/opt/cpplint/bin:$PATH
ENV PATH=/home/craftslab/opt/jdk/bin:$PATH
ENV PATH=/home/craftslab/opt/spotbugs/bin:$PATH
ENV JAVA_HOME=/home/craftslab/opt/jdk
RUN mkdir -p ~/.local/bin && \
    mkdir -p ~/opt
RUN curl -L https://download.java.net/openjdk/jdk17/ri/openjdk-17+35_linux-x64_bin.tar.gz -o openjdk.tar.gz && \
    tar zxvf openjdk.tar.gz && \
    mv jdk-17 ~/opt/jdk && \
    rm -rf openjdk.tar.gz
RUN curl -L https://github.com/checkstyle/checkstyle/releases/download/checkstyle-10.17.0/checkstyle-10.17.0-all.jar -o checkstyle.jar && \
    curl -L https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml -o google_checks.xml && \
    mkdir -p ~/opt/checkstyle/{etc,lib} && \
    mv google_checks.xml ~/opt/checkstyle/etc/ && \
    mv checkstyle.jar ~/opt/checkstyle/lib/
RUN curl -L https://github.com/spotbugs/spotbugs/releases/download/4.8.6/spotbugs-4.8.6.tgz -o spotbugs.tgz && \
    tar zxvf spotbugs.tgz && \
    mv spotbugs-4.8.6 ~/opt/spotbugs && \
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
RUN curl -L https://github.com/koalaman/shellcheck/releases/download/v0.10.0/shellcheck-v0.10.0.linux.x86_64.tar.xz -o shellcheck.tar.xz && \
    tar Jxvf shellcheck.tar.xz && \
    chmod +x shellcheck-v0.10.0/shellcheck && \
    mv shellcheck-v0.10.0/shellcheck ~/.local/bin/ && \
    rm -rf shellcheck*
RUN curl -L https://github.com/mrtazz/checkmake/releases/download/0.2.2/checkmake-0.2.2.linux.amd64 -o checkmake && \
    chmod +x checkmake && \
    mv checkmake ~/.local/bin/
RUN curl -L https://github.com/devops-lintflow/cpplint/archive/refs/heads/main.zip -o cpplint.zip && \
    unzip cpplint.zip && \
    pushd cpplint-main && \
    pyinstaller --clean --name cpplint -F cpplint.py && \
    chmod +x dist/cpplint && \
    popd && \
    mkdir -p ~/opt/cpplint/bin && \
    mv cpplint-main/dist/cpplint ~/opt/cpplint/bin/ && \
    rm -rf cpplint*
RUN curl -L https://github.com/devops-lintflow/lintwork/archive/refs/heads/main.zip -o lintwork.zip && \
    unzip lintwork.zip && \
    mv lintwork-main src && \
    cd src; make install; cd .. && \
    cp src/dist/* . && \
    cp src/lintwork/config/*.yml . && \
    sudo rm -rf src *.zip
