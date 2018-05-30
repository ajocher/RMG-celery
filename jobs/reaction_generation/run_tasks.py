import time
import sys
import itertools

from celery_framework.reaction_generation import simple_react

if __name__ == '__main__':

    n_cp = int(sys.argv[1])
    n_iter = int(sys.argv[2])
    
    result = simple_react.delay(n_cp, n_iter)
    
    # at this time, our task is not finished, so it will return False
    print 'Task state:', result.state
    
    result.get(timeout=45000)
    # print 'Task result: ', result.result

    print 'Task state:', result.state

#    print 'Task result: ', result.result
#    # sleep 10 seconds to ensure the task has been finished
#    time.sleep(10)
#    
#    # now the task should be finished and ready method will return True
#    print 'Task finished? ', result.ready()
#    print 'Task result: ', result.result
#
#    # sleep 10 seconds to ensure the task has been finished
#    time.sleep(10)
#    
#    # now the task should be finished and ready method will return True
#    print 'Task finished? ', result.ready()
#    print 'Task result: ', result.result

