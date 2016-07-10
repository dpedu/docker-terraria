FROM ubuntu:trusty

#RUN sed -i -E 's/deb http:\/\/archive.ubuntu.com/deb http:\/\/debmirror.services.davepedu.com:8080/' /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y screen mono-complete wget unzip supervisor python3-requests && \
    wget -O /tmp/terraria.zip https://github.com/NyxStudios/TShock/releases/download/v4.3.16/tshock_4.3.16.zip && \
    cd /tmp && \
    unzip terraria.zip && \
    rm terraria.zip && \
    mkdir -p /opt/terraria/tshock && \
    mv * /opt/terraria

ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf
ADD supervisor-terraria.conf /etc/supervisor/conf.d/terraria.conf
ADD config.json /opt/terraria/tshock/config.json
ADD cli.py /usr/local/bin/trcli
ADD start /start

EXPOSE 7777
EXPOSE 7878

ENTRYPOINT ["/start"]
