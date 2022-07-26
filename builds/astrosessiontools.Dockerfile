FROM quay.io/kernel-qe-hw/python:latest
LABEL maintainer="Oliver Gutiérrez <ogutsua@gmail.com>"
LABEL name=astrosessiontools
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir .
RUN rm -rfv /root/.cache /root/.npm "/var/cache/yum/"* "/var/cache/dnf/"* /var/log/dnf* /var/log/yum.* || true
ENTRYPOINT ["astro_session_tools"]
