FROM areddy1/flask_nginx:latest

COPY . /home/srv
WORKDIR /home/srv

RUN chmod +x ./run.sh
CMD [ "./run.sh" ]
