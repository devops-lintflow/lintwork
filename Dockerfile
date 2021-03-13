FROM craftslab/androiddocker:android-30

USER root
RUN apt update && \
    apt install -y upx
RUN ln -s /usr/bin/pip3 /usr/bin/pip && \
    ln -s /usr/bin/python3 /usr/bin/python
RUN python -m pip install -U pip

USER craftslab
WORKDIR /home/craftslab
ENV PATH /home/craftslab/.local/bin:$PATH
RUN mkdir src
COPY . src
RUN cd src; make install; cd .. && \
    cp src/dist/* . && \
    cp src/lintwork/config/*.yml . && \
    sudo rm -rf src
