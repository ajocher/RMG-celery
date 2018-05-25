#!/bin/bash
rm -rf debug/

n_cp=2100
n_iter=2
source activate rmg_celery_env
#python reaction_generation.py
#python -m scoop -n 6 --debug reaction_generation.py ${n_cp} ${n_iter}
python -m scoop --debug reaction_generation.py ${n_cp} ${n_iter}
source deactivate

