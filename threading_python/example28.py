# SuperFastPython.com
# example of using a semaphore
from time import sleep
from random import random
from threading import Thread
from threading import Semaphore

# target function
def task(semaphore, number):
    # attempt to acquire the semaphore
    with semaphore:
        # process
        value = random()
        sleep(value)
        # report result
        print(f'Thread {number} got {value}')

# create a semaphore
semaphore = Semaphore(2)
# create a suite of threads
for i in range(10):
    worker = Thread(target=task, args=(semaphore, i))
    worker.start()
# wait for all workers to complete...
