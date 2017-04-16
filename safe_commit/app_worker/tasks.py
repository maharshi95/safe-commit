# Author: Maharshi Gor
# from __future__ import absolute_import
from safe_commit.celery import app


@app.task(name='factorial')
def factorial(n: int):
    p = 1
    for i in range(1, n + 1):
        p *= i
    print('{}! = {}'.format(n, p))
    return p
