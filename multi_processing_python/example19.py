# SuperFastPython.com
# example of reporting the number of logical cpu cores
from multiprocessing import cpu_count
# get the number of cpu cores
num_cores = cpu_count()
# report details
print(num_cores)
