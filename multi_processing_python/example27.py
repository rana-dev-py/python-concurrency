# SuperFastPython.com
# example of using a semaphore
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Semaphore

# target function
def task(semaphore, number):
    # attempt to acquire the semaphore
    with semaphore:
        # simulate computational effort
        value = random()
        sleep(value)
        # report result
        print(f'Process {number} got {value}')

# entry point
if __name__ == '__main__':
    # create the shared semaphore
    semaphore = Semaphore(2)
    # create processes
    processes = [Process(target=task, args=(semaphore, i)) for i in range(10)]
    # start child processes
    for process in processes:
        process.start()
    # wait for child processes to finish
    for process in processes:
        process.join()
