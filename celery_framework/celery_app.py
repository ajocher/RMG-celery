
"""
This module creates the Celery instance (sometimes referred to as the app). 
To use Celery within RMG you simply import this instance.
"""

from __future__ import absolute_import, unicode_literals
from celery import Celery

# The broker argument specifies the URL of the broker to use. Here, RabbitMQ.
# The backend argument specifies the result backend to use. It's used to keep
# track of task state and results.
# The include argument is a list of modules to import when the worker starts.
app = Celery('celery_framework',
             broker='pyamqp://',
             backend = 'rpc://',
             include=['celery_framework.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

###############################################################################
if __name__ == '__main__':
    app.start()

