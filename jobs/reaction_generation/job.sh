

# Activate Python environment and run program
source activate rmg_celery_env
echo "Python tasks are now executing."
python run_tasks.py
echo "Python tasks are now completed."
source deactivate