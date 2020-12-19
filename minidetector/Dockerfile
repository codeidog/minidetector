FROM python:3.9.1-buster
ENV DB_SERVER=db
ENV DB_NAME=minidetector
ENV DB_USER=detector
ENV DB_PWD=passw123

#Copy and install dependencies
RUN mkdir /opt/minidetctor
COPY bin/setup.py /opt/minidetctor
COPY bin/README.md /opt/minidetctor
WORKDIR /opt/minidetctor
RUN python3 /opt/minidetctor/setup.py install


#Copy binaries
COPY bin /opt/minidetctor
ENTRYPOINT [ "python3", "main.py" ]
