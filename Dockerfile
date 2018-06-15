FROM ubuntu:latest

RUN apt-get update

# update and install dependencies
RUN apt-get install -y python python-pip python-virtualenv gunicorn

# change workdir
RUN mkdir -p /opt/app
COPY . /opt/app
WORKDIR /opt/app

# install python dependencies
RUN pip install -r /opt/app/requirements.txt

EXPOSE 5000

# start application
CMD ["gunicorn", "--config", "gunicorn_config.py", "main:app"]