FROM ubuntu:16.04
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' shroud

#securityRestrictions
RUN chown -R root:shroud /home/shroud/
RUN chmod 750 /home/shroud
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/shroud/

COPY shroud /home/shroud
COPY flag /home/shroud

RUN chown root:shroud /home/shroud/flag
RUN chmod 440 /home/shroud/flag

EXPOSE 40000
CMD su shroud -c "socat -T10 TCP-LISTEN:40000,reuseaddr,fork EXEC:/home/shroud/shroud"