FROM python:3.6.7

# Setup flask application
RUN mkdir -p /deploy/app
COPY app /deploy/app
RUN pip3 install -r /deploy/app/requirements.txt
RUN pip3 install gunicorn
WORKDIR /deploy/app

# Start gunicorn
CMD ["gunicorn","-w", "4", "-b", "0.0.0.0:8000", "main:app"]
