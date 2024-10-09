# SuperFastPython.com
# list all active child processes
from multiprocessing import active_children
# get a list of all active child processes
children = active_children()
# report a count of active children
print(f'Active Children Count: {len(children)}')
# report each in turn
for child in children:
    print(child)
