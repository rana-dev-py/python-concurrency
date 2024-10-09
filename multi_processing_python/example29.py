# SuperFastPython.com
# example of using a barrier with processes
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Barrier

# target function to prepare some work
def task(barrier, number):
    # generate a unique value
    value = random() * 10
    # block for a moment
    sleep(value)
    # report result
    print(f'Process {number} done, got: {value}', flush=True)
    # wait on all other processes to complete
    barrier.wait()

# entry point
if __name__ == '__main__':
    # create a barrier
    barrier = Barrier(5 + 1)
    # create the worker processes
    for i in range(5):
        # start a new process to perform some work
        worker = Process(target=task, args=(barrier, i))
        worker.start()
    # wait for all processes to finish
    print('Main process waiting on all results...')
    barrier.wait()
    # report once all processes are done
    print('All processes have their result')
