
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y \
    install sudo xvfb \
    git wget python-virtualenv python3 python3-pip python3-venv python3-dev netpbm\
    python-pyqt5 ghostscript libffi-dev libjpeg-turbo-progs \
    python3-dev cmake  \
    libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev \
    python-tk python3-tk \
    libharfbuzz-dev libfribidi-dev && apt-get clean


# Setup flask application
RUN mkdir -p /deploy/app
COPY app /deploy/app
RUN pip3 install -r /deploy/app/requirements.txt
RUN pip3 install Pillow
RUN pip3 install gunicorn
run pip3 install dhash
WORKDIR /deploy/app

EXPOSE 9000

# Start gunicorn
CMD ["gunicorn","-w", "5", "-b", "0.0.0.0:9000", "application:app"]
