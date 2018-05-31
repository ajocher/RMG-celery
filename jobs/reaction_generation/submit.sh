#!/bin/bash
#SBATCH -p debug                # partition (queue)
#SBATCH -J TestCelery               # Job name
#SBATCH -o slurm.%N.%j.out      # STDOUT
#SBATCH -e slurm.%N.%j.err      # STDERR

#SBATCH -t 10-24:00:00  # time (D-HH:MM)
#SBATCH -n 6           # number of cores, default is one task per node
##SBATCH -w node01
#SBATCH -N 1            # number of nodes
#SBATCH --mem=10000    # memory pool for all cores

# Comments:
# Request run time on RMG-Server
# Node01-04, 12 cores/node, 2 threads/core, 96 GB/node
# Node05-08, 20 cores/node, 2 threads/core, 128 GB/node

rm *.log *.pid *.err *.out

# Activate Python environment and run program
source activate rmg_celery_env


# Start celery worker.
celery multi start w1 -A celery_framework.celery_app:app \
 --loglevel=debug --logfile=nI.log

#celery multi start w1 -A celery_framework.celery_app:app --concurrency=2 \
# --maxtasksperchild 5000 --loglevel=debug --logfile=nI.log

#celery worker -A celery_framework.celery_app:app --concurrency=4  -l info

#celery flower --basic_auth=ajocher:newPW,kehang:newPW multi start w1 -A celery_framework.celery_app:app --concurrency=2 \
# --loglevel=debug --logfile=nI.log # \
## --pidfile=n.pid \
## --logfile=nI.log


# Activate Python environment and run program.
source activate rmg_celery_env
echo "Python tasks are now executing."

n_cp=10 #2500
n_iter=1
python run_tasks.py ${n_cp} ${n_iter}

echo "Python tasks are now completed."


# Shut celery worker down.
celery multi stopwait w1 -l info
source deactivate

