FROM python:3.7-slim-stretch

RUN apt-get -y update
RUN apt-get install -y python3-pip

RUN pip3 install flask

COPY . /home/server
WORKDIR /home/server

CMD echo "hello from dockerfile"
ENTRYPOINT [ "python3", "app.py" ]
