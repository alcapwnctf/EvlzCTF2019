FROM ubuntu:16.04
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' multi

#securityRestrictions
RUN chown -R root:multi /home/multi/
RUN chmod 750 /home/multi
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/multi/

COPY multi /home/multi
COPY flag /home/multi

RUN chown root:multi /home/multi/flag
RUN chmod 440 /home/multi/flag

EXPOSE 31337
CMD su multi -c "socat -T10 TCP-LISTEN:31337,reuseaddr,fork EXEC:/home/multi/multi"