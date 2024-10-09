# SuperFastPython.com
# example of setting a thread to be a daemon via the property
from threading import Thread
# create a thread
thread = Thread()
# configure the thread to be a daemon
thread.daemon = True
# report if the thread is a daemon
print(thread.daemon)
