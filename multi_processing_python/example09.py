# SuperFastPython.com
# example of checking the exit status of a child process
from time import sleep
from multiprocessing import Process

# function to execute in a new process
def task():
    sleep(1)

# entry point
if __name__ == '__main__':
    # create the process
    process = Process(target=task)
    # report the exit status
    print(process.exitcode)
    # start the process
    process.start()
    # report the exit status
    print(process.exitcode)
    # wait for the process to finish
    process.join()
    # report the exit status
    print(process.exitcode)
