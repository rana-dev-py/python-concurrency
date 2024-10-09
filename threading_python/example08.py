# SuperFastPython.com
# example of reporting the native thread identifier
from threading import Thread
# create the thread
thread = Thread()
# report the native thread identifier
print(thread.native_id)
# start the thread
thread.start()
# report the native thread identifier
print(thread.native_id)
