FROM python:3.9.0 as build-stage
WORKDIR /usr/src/app
COPY . .
RUN apt update && \
    apt install -y upx
RUN make install

FROM craftslab/androiddocker:android-30 as production-stage
USER craftslab
WORKDIR /home/craftslab
COPY --from=build-stage /usr/src/app/dist/* ./
COPY --from=build-stage /usr/src/app/lintaosp/config/*.yml ./
