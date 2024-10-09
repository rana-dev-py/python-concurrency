# SuperFastPython.com
# example of wait/notify with a condition for processes
from time import sleep
from multiprocessing import Process
from multiprocessing import Condition

# target function to prepare some work
def task(condition):
    # block for a moment
    sleep(1)
    # notify a waiting process that the work is done
    print('Child process sending notification...', flush=True)
    with condition:
        condition.notify()
    # do something else...
    sleep(1)

# entry point
if __name__ == '__main__':
    # create a condition
    condition = Condition()
    # wait to be notified that the data is ready
    print('Main process waiting for data...')
    with condition:
        # start a new process to perform some work
        worker = Process(target=task, args=(condition,))
        worker.start()
        # wait to be notified
        condition.wait()
    # we know the data is ready
    print('Main process all done')
