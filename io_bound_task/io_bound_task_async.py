# import asyncio




""" example 1 """
# async def fetch_data():
#     print("Fetching data...")
#     await asyncio.sleep(2)  
#     print("Data fetched!")

# async def main():
#     await asyncio.gather(fetch_data(), fetch_data(), fetch_data())

# asyncio.run(main())



""" example 2 

asyncio.gather(): Allows you to run multiple I/O-bound tasks concurrently, improving efficiency in situations where tasks are waiting for external resources (like API responses).
"""

import aiohttp
import asyncio

# Fetch data from the JSONPlaceholder API
async def fetch_data(session, url):
    async with session.get(url) as response:
        data = await response.json()
        print(f"Fetched data from {url}")
        return data

# Main function to gather multiple requests
async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print("\n\n >>  " , result)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
