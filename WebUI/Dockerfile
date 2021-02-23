FROM python:3.9.2-alpine
ENV DB_SERVER=
ENV DB_NAME=
ENV DB_USER=
ENV DB_PWD=
ENV PORT=8080

#Copy and install dependencies
RUN mkdir /opt/webui
COPY bin/requirements.txt /opt/webui
WORKDIR /opt/webui

#Install psycog2 dependencies
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


#Copy binaries
COPY bin /opt/webui
EXPOSE 8080
ENTRYPOINT gunicorn --bind "0.0.0.0:$PORT" --access-logfile - wsgi:app
