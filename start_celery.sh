
# Activate Python environment and run program
source activate rmg_celery_env

# Start celery worker.
celery multi start w1 -A celery_framework.tasks --loglevel=info