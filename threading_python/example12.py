# SuperFastPython.com
# example of setting the thread name via the property
from threading import Thread
# create a thread
thread = Thread()
# set the name
thread.name = 'MyThread'
# report thread name
print(thread.name)
