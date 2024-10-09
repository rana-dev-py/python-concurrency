# SuperFastPython.com
# example of getting the current thread for the main thread
from threading import current_thread
# get the main thread
thread = current_thread()
# report properties for the main thread
print(f'name={thread.name}, daemon={thread.daemon}, id={thread.ident}')
