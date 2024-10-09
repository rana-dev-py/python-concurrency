# SuperFastPython.com
# example of a deadlock caused by a thread waiting on itself
from threading import Thread
from threading import Lock

# task2 to be executed in a new thread
def task2(lock):
    print('Thread acquiring lock again...')
    with lock:
        # will never get here
        pass

# task1 to be executed in a new thread
def task1(lock):
    print('Thread acquiring lock...')
    with lock:
        task2(lock)

# create the mutex lock
lock = Lock()
# create and configure the new thread
thread = Thread(target=task1, args=(lock,))
# start the new thread
thread.start()
# wait for threads to exit...
thread.join()
