# SuperFastPython.com
# retrieve the current thread within
from threading import Thread
from threading import current_thread

# function to get the current thread
def task():
    # get the current thread
    thread = current_thread()
    # report the name
    print(thread.name)

# create a thread
thread = Thread(target=task)
# start the thread
thread.start()
# wait for the thread to exit
thread.join()
