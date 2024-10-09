# SuperFastPython.com
# example of stopping a new process
from time import sleep
from multiprocessing import Process
from multiprocessing import Event

# custom task function
def task(event):
    # execute a task in a loop
    for i in range(5):
        # block for a moment
        sleep(1)
        # check for stop
        if event.is_set():
            break
        # report a message
        print('Worker process running...', flush=True)
    print('Worker closing down', flush=True)

# entry point
if __name__ == '__main__':
    # create the event
    event = Event()
    # create and configure a new process
    process = Process(target=task, args=(event,))
    # start the new process
    process.start()
    # block for a while
    sleep(3)
    # stop the worker process
    print('Main stopping process')
    event.set()
    # wait for the new process to finish
    process.join()