#!/bin/bash
rm -rf debug/

n_cp=1
n_iter=1
source activate rmg_celery_env
#python reaction_generation.py
#python -m scoop -n 6 --debug reaction_generation.py ${n_cp} ${n_iter}
python -m scoop --debug reaction_generation.py ${n_cp} ${n_iter}
source deactivate

