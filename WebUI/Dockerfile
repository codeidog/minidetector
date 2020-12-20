FROM python:3.9.1-buster
ENV DB_SERVER=db
ENV DB_NAME=minidetector
ENV DB_USER=detector
ENV DB_PWD=passw123
ENV PORT=8080
#Copy and install dependencies
RUN mkdir /opt/webui
COPY bin/requirements.txt /opt/webui
WORKDIR /opt/webui
RUN pip3 install -r requirements.txt


#Copy binaries
COPY bin /opt/webui
EXPOSE 8080
#ENTRYPOINT [ "python3", "main.py" ]
ENTRYPOINT gunicorn --bind "0.0.0.0:$PORT" --access-logfile - wsgi:app
