FROM ubuntu:16.04
	
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y python3 socat build-essential

RUN adduser --disabled-password --gecos '' magic
RUN mkdir /home/magic/LEVEL1
RUN mkdir /home/magic/LEVEL2
RUN mkdir /home/magic/LEVEL3
RUN mkdir /home/magic/LEVEL4
RUN chown -R root:magic /home/magic/
RUN chmod 770 /home/magic
RUN export TERM=xterm

WORKDIR /home/magic/


COPY magic.py /home/magic
RUN chmod 770 /home/magic/magic.py

EXPOSE 60000
CMD socat -T10 TCP-LISTEN:60000,reuseaddr,fork EXEC:/home/magic/magic.py
