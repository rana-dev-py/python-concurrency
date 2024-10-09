# SuperFastPython.com
# example of reporting the name of the main process
from multiprocessing import current_process
# get the main process
process = current_process()
# report the name of the main process
print(process.name)
