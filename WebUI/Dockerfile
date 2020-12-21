FROM python:3.9.1
#ENV DB_SERVER=
#ENV DB_NAME=
#ENV DB_USER=
#ENV DB_PWD=
ENV PORT=8080

#Copy and install dependencies
RUN mkdir /opt/webui
COPY bin/requirements.txt /opt/webui
WORKDIR /opt/webui
RUN pip3 install -r requirements.txt


#Copy binaries
COPY bin /opt/webui
EXPOSE 8080
ENTRYPOINT gunicorn --bind "0.0.0.0:$PORT" --access-logfile - wsgi:app
