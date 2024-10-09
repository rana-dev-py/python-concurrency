# SuperFastPython.com
# example of setting the process name via the property
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create a process
    process = Process()
    # set the name
    process.name = 'MyProcess'
    # report process name
    print(process.name)
