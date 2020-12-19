FROM postgres:13
ENV DB_NAME=minidetector
ENV DB_USER=detector
ENV DB_PWD=passw123
ENV POSTGRES_PASSWORD=password
COPY initdb.sh /docker-entrypoint-initdb.d
RUN  chmod +x /docker-entrypoint-initdb.d//initdb.sh 