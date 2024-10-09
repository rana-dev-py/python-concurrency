# SuperFastPython.com
# example of setting the thread name in the constructor
from threading import Thread
# create a thread with a custom name
thread = Thread(name='MyThread')
# report thread name
print(thread.name)
