# SuperFastPython.com
# report the native id for the current thread
from threading import get_native_id
# get the native id for the current thread
identifier = get_native_id()
# report the thread id
print(identifier)
