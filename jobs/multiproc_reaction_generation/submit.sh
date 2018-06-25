#!/bin/bash
#SBATCH -p debug                # partition (queue)
#SBATCH -J Multiproc               # Job name
#SBATCH -o slurm.%N.%j.out      # STDOUT
#SBATCH -e slurm.%N.%j.err      # STDERR

#SBATCH -t 10-24:00:00  # time (D-HH:MM)
#SBATCH -n 24          # number of cores, default is one task per node
#SBATCH -w node03
#SBATCH -N 1            # number of nodes
#SBATCH --mem=10000    # memory pool for all cores

# Comments:
# Request run time on RMG-Server
# Node01-04, 12 cores/node, 2 threads/core, 96 GB/node
# Node05-08, 20 cores/node, 2 threads/core, 128 GB/node

# Activate Python environment and run program.
source activate rmg_celery_env
echo "Python tasks are now executing."

n_cp=24
n_iter=10
n_pool=12
python run_tasks.py ${n_cp} ${n_iter} ${n_pool}

echo "Python tasks are now completed."

source deactivate

