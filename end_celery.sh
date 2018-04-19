
source activate rmg_celery_env
celery multi stopwait w1 -A celery_framework.tasks -l info
source deactivate