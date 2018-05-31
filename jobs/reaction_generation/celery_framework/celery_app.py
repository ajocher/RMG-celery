
"""
This module creates the Celery instance (sometimes referred to as the app). 
To use Celery within RMG you simply import this instance.
"""

from __future__ import absolute_import, unicode_literals
from celery import Celery

# track of task state and results.
# Note: cannot use guest for authenticating with broker unless on localhost
# 18.172.0.124 is the IP of RMG.MIT.EDU
SERVERHOST = '18.172.0.124' # rmg.mit.edu
#SERVERHOST = 'localhost'

app = Celery('celery_framework',

             # The broker argument specifies the URL of the broker to use. Here, RabbitMQ.
#             broker='pyamqp://',
#             broker='amqp://user:PW@localhost:5672/greylock',
             broker='amqp://user:PW@{}:5672/greylock'.format(SERVERHOST),
             
             # The backend argument specifies the result backend to use. It's used to keep
#             backend = 'rpc://',
             backend = 'rpc://{}:6379'.format(SERVERHOST),
             
             # Maximum amount of resident memory, in kilobytes, that 
             # may be consumed by a worker before it will be replaced 
             # by a new worker.
             worker_max_memory_per_child = 12000,  # 12MB
             
             # The include argument is a list of modules to import when the worker starts.
             include=['celery_framework.mini_tasks',
             		  'celery_framework.reaction_generation'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    result_serializer='pickle',
    accept_content=['pickle', 'json']
)

###############################################################################
if __name__ == '__main__':
    app.start()

