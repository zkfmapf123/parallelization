import asyncio
import threading
import time

LOOP = asyncio.get_event_loop()


async def worker_1(lock, num):
    print("worker_1 start >> ", num)
    # time.sleep(2) >> 순차처리
    # await asyncio.sleep(2) >> 병렬처리

    async with lock:
        print("worker_1 acquired lock")
        await asyncio.sleep(3)
    print("worker_1 end")


async def worker_2(lock, num):
    print("worker_2 start >> ", num)

    async with lock:
        print("worker_2 acquired lock")
        await asyncio.sleep(3)
    print("worker_2 end")


if __name__ == "__main__":
    lock = asyncio.Lock()

    workers = []
    for i in range(100):
        if i % 2 == 0:
            workers.append(worker_1(lock, i))
        else:
            workers.append(worker_2(lock, i))

    tasks: list[asyncio.ensure_future] = [
        asyncio.ensure_future(worker) for worker in workers]

    LOOP.run_until_complete(asyncio.wait(tasks))
