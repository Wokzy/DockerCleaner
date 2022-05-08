FROM ubuntu:focal

RUN apt update && apt install -y python3

ADD ./server.py bin
ADD ./client.py bin

ENTRYPOINT ["python3", "/bin/server.py"]
#ENTRYPOINT ["ls"]