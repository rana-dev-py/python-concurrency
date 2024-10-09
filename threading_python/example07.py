# SuperFastPython.com
# example of reporting the thread identifier
from threading import Thread
# create the thread
thread = Thread()
# report the thread identifier
print(thread.ident)
# start the thread
thread.start()
# report the thread identifier
print(thread.ident)
