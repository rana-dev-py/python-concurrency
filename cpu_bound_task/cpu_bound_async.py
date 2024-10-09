
"""

asyncio does not provide true parallelism for CPU-bound tasks. Since it operates in a single thread and single event loop, only one task can be executing CPU instructions at any time.
For CPU-bound tasks (e.g., heavy computations), asyncio will not improve performance, as it does not utilize multiple CPU cores. When a CPU-bound task starts, 
it will block the event loop, preventing other tasks from running.

Note :In Python, asyncio is not designed for CPU-bound tasks

"""

import asyncio
async def compute():
    print("Computing...")
    # Simulate a CPU-bound task
    result = 0
    for i in range(10**7):
        result += i
    print("Computation complete!")

async def main():
    await asyncio.gather(compute(), compute())

asyncio.run(main())
