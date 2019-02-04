FROM ubuntu:16.04
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' attackd

#securityRestrictions
RUN chown -R root:attackd /home/attackd/
RUN chmod 750 /home/attackd
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/attackd/

COPY attackd /home/attackd
COPY flag /home/attackd

RUN chown root:attackd /home/attackd/flag
RUN chmod 440 /home/attackd/flag

EXPOSE 31336
CMD su attackd -c "socat -T10 TCP-LISTEN:31336,reuseaddr,fork EXEC:/home/attackd/attackd"