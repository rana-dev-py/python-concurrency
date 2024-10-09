# SuperFastPython.com
# example of getting the parent process of the main process
from multiprocessing import parent_process
# get the the parent process
process = parent_process()
# report details
print(process)
