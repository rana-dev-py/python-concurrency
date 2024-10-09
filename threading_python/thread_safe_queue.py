import queue
import threading

q = queue.Queue()
print("now queuw is  :  ", q)
def producer():
    for i in range(5):
        q.put(i)
        print("now queuw is  :  ", (q))
        print(f"Produced: {i}")

def consumer():
    while True:
        item = q.get()
        print(f"Consumed: {item}")
        if item == 4:
            break

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
