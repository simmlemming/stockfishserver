FROM ubuntu:latest

RUN apt-get update; apt-get -y install python3 pip
RUN pip3 install stockfish

WORKDIR /app
COPY stockfish-ubuntu-20.04-x86-64 .
COPY app .

CMD ["python3", "main.py"]