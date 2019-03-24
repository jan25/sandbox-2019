FROM python:3.7-slim-stretch

RUN apt-get -y update
RUN apt-get install -y python3-pip

RUN pip3 install flask
RUN pip3 install requests

COPY . /home/server
WORKDIR /home/server

# Starts Flask server on port 5000
ENTRYPOINT [ "python3", "app.py" ]