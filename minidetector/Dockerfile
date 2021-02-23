FROM python:3.9.2-alpine
ENV DB_SERVER=
ENV DB_NAME=
ENV DB_USER=
ENV DB_PWD=

#Copy and install dependencies
RUN mkdir /opt/minidetctor
COPY bin/requirements.txt /opt/minidetctor
WORKDIR /opt/minidetctor

#Install psycog2 dependencies
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


#Copy binaries
COPY bin /opt/minidetctor
ENTRYPOINT [ "python3", "main.py" ]
