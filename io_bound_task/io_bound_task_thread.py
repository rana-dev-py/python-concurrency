import threading
import time
import requests

# I/O-bound task: Fetching data from an external API
def fetch_data(url):
    print(f"Thread {threading.current_thread().name} starting request to {url}")
    response = requests.get(url)  # Simulate network I/O-bound task
    print(f"Thread {threading.current_thread().name} received response from {url}")
    return response.text

# Function to handle threading for I/O-bound tasks
def run_io_bound_tasks(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_data, args=(url,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # URLs to simulate I/O-bound tasks (network requests)
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    start_time = time.time()
    
    # Run I/O-bound tasks in parallel using threading
    run_io_bound_tasks(urls)
    
    end_time = time.time()
    
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
