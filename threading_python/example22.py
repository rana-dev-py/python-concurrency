# SuperFastPython.com
# example of an unhandled exception in a thread
from time import sleep
from threading import Thread

# target function that raises an exception
def work():
    print('Working...')
    sleep(1)
    # rise an exception
    raise Exception('Something bad happened')

# create a thread
thread = Thread(target=work)
# run the thread
thread.start()
# wait for the thread to finish
thread.join()
# continue on
print('Continuing on...')
