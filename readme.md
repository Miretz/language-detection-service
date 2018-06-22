# Language detection service

- Service is using the Flask framework
- Libraries for detection: Langid.py, Langdetect
- Can be packaged and deployed as a microservice
- Swagger API documentation and UI included

## Setup
```
pip install -r requirements.txt
```

## Run - Development mode
```
python main.py
```
Navigate to http://localhost:5000/

You should see the basic UI:

<img src="screenshots/gui.png">


## Swagger UI - API Documentation

Navigate to http://localhost:5000/api/ui/

You should see the Swagger UI:

<img src="screenshots/swagger.png">


## Run - Production mode using Gunicorn
```
gunicorn --config gunicorn_config.py main:app
```
Navigate to http://localhost:5000/

Note: Windows is not supported by Gunicorn.

## Dockerfile

- Basic Dockerfile included, please modify it to suit your needs.

### Run from docker for beginners

Install Docker on your machine. See: https://store.docker.com/


Build the container and start
```
docker build -t language-detection .
docker run -d -p 80:5000 --name language-detection language-detection
```

You can now access the application via port 80.


To stop the container:
```
docker container stop language-detection
```
