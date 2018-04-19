#!/bin/bash
rm -rf debug/

n_cp=1
n_iter=2
source activate rmg_celery_env
#python reaction_generation.py
python -m scoop -n 4 --debug reaction_generation.py ${n_cp} ${n_iter}
source deactivate

