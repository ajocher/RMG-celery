#!/bin/bash

rm *.log


# Activate Python environment and run program
source activate rmg_celery_env


# Start celery worker.
celery multi start w1 -A celery_framework.celery_app:app \
 --loglevel=info \
 --pidfile=%n.pid \
 --logfile=%n%I.log


# Activate Python environment and run program.
source activate rmg_celery_env
echo "Python tasks are now executing."

n_cp=1 #2500
n_iter=1
python run_tasks.py ${n_cp} ${n_iter}

echo "Python tasks are now completed."


# Shut celery worker down.
celery multi stopwait w1 -l info
source deactivate

