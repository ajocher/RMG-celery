#!/bin/bash
rm -rf debug/
source activate rmg_celery_env
#python reaction_generation.py
python -m scoop -n 4 --debug reaction_generation.py
source deactivate

