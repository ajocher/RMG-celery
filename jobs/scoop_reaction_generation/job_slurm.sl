#!/bin/bash
#SBATCH -p debug			# partition (queue)
#SBATCH -J scoop			# Job name
#SBATCH -o slurm.%N.%j.out	# STDOUT
#SBATCH -e slurm.%N.%j.err	# STDERR

#SBATCH -n 6				# number of requested cores
#SBATCH -w node03

WORKERS=6 					# no greater than the number of cores requested
n_cp=1
n_iter=2
hosts=$(srun bash -c hostname)
source activate rmg_celery_env
python -m scoop -n $WORKERS --host $hosts --debug reaction_generation.py ${n_cp} ${n_iter}
source deactivate