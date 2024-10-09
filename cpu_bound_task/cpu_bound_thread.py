import threading

def compute():
    print("Computing...")
    result = 0
    for i in range(10**7):
        result += i
    print("Computation complete!")

threads = []
for _ in range(3):
    t = threading.Thread(target=compute)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
