# SuperFastPython.com
# example of reusing a thread
from time import sleep
from threading import Thread

# custom target function
def task():
    # block for a moment
    sleep(1)
    # report a message
    print('Hello from the new thread')

# create a new thread
thread = Thread(target=task)
# start the thread
thread.start()
# wait for the thread to finish
thread.join()
# try and start the thread again
thread.start()
