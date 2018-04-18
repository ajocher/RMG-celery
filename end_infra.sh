
# Stop celery
celery multi stopwait w1 -A celery_framework.tasks -l info

# Stop RabbitMQ server
rabbitmqctl stop