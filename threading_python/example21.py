# SuperFastPython.com
# enumerate all active threads
import threading
# get a list of all active threads
threads = threading.enumerate()
# report the name of all active threads
for thread in threads:
    print(thread.name)
