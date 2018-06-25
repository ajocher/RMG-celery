#!/bin/bash

rm *.log

# Activate Python environment and run program.
source activate rmg_celery_env
echo "Python tasks are now executing."

n_cp=24
n_iter=4
n_pool=2
python run_tasks.py ${n_cp} ${n_iter} ${n_pool}
#mprof run -M python run_tasks.py ${n_cp} ${n_iter} ${n_pool}
#python -m memory_profiler run_tasks.py ${n_cp} ${n_iter} ${n_pool}

echo "Python tasks are now completed."

source deactivate

