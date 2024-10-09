# SuperFastPython.com
# example of setting a process to be a daemon via the property
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create a process
    process = Process()
    # configure the process to be a daemon
    process.daemon = True
    # report if the process is a daemon
    print(process.daemon)
