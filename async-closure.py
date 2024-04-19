import asyncio

async def fetch_data(url):
    response = await asyncio.get(url)
    return await response.read()

async def main():
    url1 = "https://example1.com"
    url2 = "https://example2.com"

    data1_future = asyncio.create_task(fetch_data(url1))
    data2_future = asyncio.create_task(fetch_data(url2))

    data1 = await data1_future
    data2 = await data2_future

    print(f"Data from {url1}: {data1}")
    print(f"Data from {url2}: {data2}")

if __name__ == "__main__":
    asyncio.run(main())
