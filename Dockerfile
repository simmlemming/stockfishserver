FROM ubuntu:latest

RUN apt-get update; apt-get -y install python3 pip
RUN pip3 install stockfish termcolor

WORKDIR /app
COPY stockfish-ubuntu-20.04-x86-64 .
COPY app .

CMD ["python3", "-u", "main.py", "--stockfish-bin", "./stockfish-ubuntu-20.04-x86-64"]