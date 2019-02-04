FROM ubuntu:16.04
	
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y python3 socat build-essential

RUN adduser --disabled-password --gecos '' dhke
RUN chown -R root:dhke /home/dhke/
RUN chmod 770 /home/dhke
RUN export TERM=xterm

WORKDIR /home/dhke/

COPY dhke.py /home/dhke
RUN chmod 770 /home/dhke/dhke.py

EXPOSE 50000
CMD socat -T10 TCP-LISTEN:50000,reuseaddr,fork EXEC:/home/dhke/dhke.py
