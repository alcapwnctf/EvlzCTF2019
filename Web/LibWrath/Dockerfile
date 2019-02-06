FROM python:3.6.7

# Setup flask application
RUN mkdir -p /deploy/app
COPY app /deploy/app
RUN pip3 install -r /deploy/app/requirements.txt
RUN pip3 install gunicorn
WORKDIR /deploy/app

EXPOSE 8000