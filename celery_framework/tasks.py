from __future__ import absolute_import, unicode_literals
from celery_framework.celery_app import app
import time

@app.task(ignore_result=False)
def add(x, y):
    return x + y


@app.task(ignore_result=False)
def mul(x, y):
    return x * y


@app.task(ignore_result=False)
def xsum(numbers):
    return sum(numbers)

@app.task(ignore_result=False)
def print_hello():
    print 'hello there'

@app.task(ignore_result=False)
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results

@app.task
def longtime_add(x, y):
    print 'long time task begins'
    # sleep 5 seconds
    time.sleep(5)
    print 'long time task finished'
    return x + y

