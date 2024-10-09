# SuperFastPython.com
# example of assessing whether a process is a daemon
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the daemon attribute
    print(process.daemon)
