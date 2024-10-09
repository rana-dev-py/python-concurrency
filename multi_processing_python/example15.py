# SuperFastPython.com
# example of getting the main process from a child of the main process
from multiprocessing import parent_process
from multiprocessing import Process

# function executed in a child process
def task():
    # get the parent process instance
    process = parent_process()
    # report details of the main process
    print(process)

# entry point
if __name__ == '__main__':
    # create a new process
    process = Process(target=task)
    # start the new process
    process.start()
    # wait for the new process to terminate
    process.join()
