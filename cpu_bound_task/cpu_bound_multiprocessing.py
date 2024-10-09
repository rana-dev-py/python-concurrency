import multiprocessing
import time

# CPU-bound task: A function that computes a factorial
def calculate_factorial(n):
    print(f"Process {multiprocessing.current_process().name} calculating factorial of {n}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"Process {multiprocessing.current_process().name} finished factorial of {n}")
    return result

# Function to handle multiprocessing for CPU-bound tasks
def run_multiprocessing_tasks(numbers):
    # Create a pool of processes, with each process running in parallel
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, numbers)
    return results

if __name__ == "__main__":
    numbers = [100000, 200000, 300000]  # CPU-bound tasks (large factorials)
    
    start_time = time.time()
    
    # Run CPU-bound tasks in parallel using multiprocessing
    results = run_multiprocessing_tasks(numbers)
    
    end_time = time.time()
    
    # Print only the first 10 digits of each factorial result
    for idx, result in enumerate(results, start=1):
        print(f"\n Result of factorial {idx}: {result} ")
    
    print(f"Time taken: {end_time - start_time:.2f} seconds")
