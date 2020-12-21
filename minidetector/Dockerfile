FROM python:3.9.1
ENV DB_SERVER=
ENV DB_NAME=
ENV DB_USER=
ENV DB_PWD=

#Copy and install dependencies
RUN mkdir /opt/minidetctor
COPY bin/setup.py /opt/minidetctor
WORKDIR /opt/minidetctor
RUN python3 /opt/minidetctor/setup.py install


#Copy binaries
COPY bin /opt/minidetctor
ENTRYPOINT [ "python3", "main.py" ]
