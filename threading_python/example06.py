# SuperFastPython.com
# example of assessing whether a thread is a daemon
from threading import Thread
# create the thread
thread = Thread()
# report the daemon attribute
print(thread.daemon)
