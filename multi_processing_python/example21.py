# SuperFastPython.com
# example of executing the current process within a child process
from multiprocessing import Process
from multiprocessing import current_process

# function executed in a new process
def task():
    # get the current process
    process = current_process()
    # report details
    print(process)

# entry point
if __name__ == '__main__':
    # create a new process
    process = Process(target=task)
    # start the new process
    process.start()
    # wait for the child process to terminate
    process.join()
