FROM ubuntu:latest

# update and install dependencies
RUN apt-get update
RUN apt-get install -y python3-pip default-jre-headless wget
RUN pip3 install --no-cache-dir -U pip==10.0.1

# create required directories
RUN mkdir -p /opt/app
RUN mkdir -p /opt/upload
COPY src/ /opt/app

# install python dependencies
COPY requirements.txt /opt
RUN pip install --no-cache-dir -r /opt/requirements.txt

# change workdir
WORKDIR /opt/app

# download the Tika jar file
RUN wget -q http://www-eu.apache.org/dist/tika/tika-app-1.18.jar -O lib/tika-app-1.18.jar

EXPOSE 5000

# start application
CMD ["gunicorn", "--config", "gunicorn_config.py", "main:app"]