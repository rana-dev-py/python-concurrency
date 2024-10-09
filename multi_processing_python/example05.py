# SuperFastPython.com
# example of accessing the child process name
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the process name
    print(process.name)
