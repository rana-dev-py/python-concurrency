# SuperFastPython.com
# example of a livelock
from time import sleep
from threading import Thread
from threading import Lock

# task for worker threads
def task(number, lock1, lock2):
    # loop until the task is completed
    while True:
        # acquire the first lock
        with lock1:
            # wait a moment
            sleep(0.1)
            # check if the second lock is available
            if lock2.locked():
                print(f'Task {number} cannot get the second lock, giving up...')
            else:
                # acquire lock2
                with lock2:
                    print(f'Task {number} made it, all done.')
                    break

# create locks
lock1 = Lock()
lock2 = Lock()
# create threads
thread1 = Thread(target=task, args=(0, lock1, lock2))
thread2 = Thread(target=task, args=(1, lock2, lock1))
# start threads
thread1.start()
thread2.start()
# wait for threads to finish
thread1.join()
thread2.join()
