

# Activate Python environment and run program
source activate celery
echo "Python tasks are now executing."
python celery_framework/run_tasks.py
echo "Python tasks are now completed."
source deactivate