# SuperFastPython.com
# example of setting a process to be a daemon via the constructor
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create a daemon process
    process = Process(daemon=True)
    # report if the process is a daemon
    print(process.daemon)
