FROM debian:bullseye 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip && \
    mkdir /app && \
    useradd -ms /bin/bash runuser
COPY --chown=runuser:runuser . /app 
RUN pip install --upgrade -r /app/requirements.txt
ENV FILENAME "sample-file.txt"
USER runuser 
SHELL ["/bin/bash", "-c"]
WORKDIR /app
CMD /usr/bin/python3 /app/main.py ${FILENAME}
