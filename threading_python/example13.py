# SuperFastPython.com
# example of setting a thread to be a daemon via the constructor
from threading import Thread
# create a daemon thread
thread = Thread(daemon=True)
# report if the thread is a daemon
print(thread.daemon)
