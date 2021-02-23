FROM postgres:13.2-alpine
ENV DB_NAME=
ENV DB_USER=
ENV DB_PWD=
COPY initdb.sh /docker-entrypoint-initdb.d
RUN  chmod +x /docker-entrypoint-initdb.d//initdb.sh 