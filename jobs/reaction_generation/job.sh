#!/bin/bash

rm *.log

# Activate Python environment and run program
source activate rmg_celery_env

# Start celery worker.
celery multi start w1 -A celery_framework.celery_app:app --loglevel=info

# Activate Python environment and run program.
source activate rmg_celery_env
echo "Python tasks are now executing."
python run_tasks.py
echo "Python tasks are now completed."

# Shut celery worker down.
celery multi stopwait w1 -l info
source deactivate

