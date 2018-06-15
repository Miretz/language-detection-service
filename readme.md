# Language detection service

- Service is using the Flask framework
- Libraries for detection: Langid.py, Langdetect

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

<img src="screenshots/ui.png">


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