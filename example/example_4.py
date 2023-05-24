import asyncio
import time

import aiohttp

loop = asyncio.get_event_loop()


# Bad Practice (BAD)
# async def hello(url):
#     print(requests.get(url).content)
#     print(time.time())

# Best Practice (GOOD)
async def hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(await resp.text())
            print(time.time())


if __name__ == "__main__":
    loop.run_until_complete(asyncio.wait([
        asyncio.ensure_future(hello("http://httpbin.org/headers")) for _ in range(100)]))
