# SuperFastPython.com
# example of getting the parent process of a child process
from multiprocessing import parent_process
from multiprocessing import Process

# function to execute in a new process
def task():
    # get the the parent process
    process = parent_process()
    # report details
    print(process)

# entry point
if __name__ == '__main__':
    # create a new process
    process = Process(target=task)
    # start the new process
    process.start()
    # wait for the new process to terminate
    process.join()
