# SuperFastPython.com
# example of getting the main process from the main process
from multiprocessing import current_process
# get the process instance
process = current_process()
# report details of the main process
print(process)
