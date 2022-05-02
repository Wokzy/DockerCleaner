FROM ubuntu:focal

RUN apt update && apt install -y python3

ADD ./client.py bin

ENTRYPOINT ["python3", "/bin/client.py"]