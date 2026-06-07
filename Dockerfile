FROM ubuntu:latest
LABEL authors="viinna"

ENTRYPOINT ["top", "-b"]