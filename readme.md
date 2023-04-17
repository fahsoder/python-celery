# python celery

## installation
- pip install flask celery

## execute
### rabbimq server
- docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

### celery worker
- celery -A tasks worker --pool=solo -l info

### flask application
- python app.py

### endpoint call
- curl --location 'localhost:5000/'