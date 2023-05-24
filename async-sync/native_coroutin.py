import asyncio
import concurrent.futures
import threading
import time

loop = asyncio.get_event_loop()


def worker_thread(num):
    """
        normal worker thread
    """
    print("start")

    print(num)
    time.sleep(2)
    print("end")
    pass


async def async_worker():
    """
        worker thread use async
    """
    print("start")

    await asyncio.sleep(2)
    print("end")


if __name__ == "__main__":
    # 병렬처리
    coros: list[async_worker()] = [async_worker() for _ in range(8)]
    tasks: list[asyncio.ensure_future] = [
        asyncio.ensure_future(c) for c in coros]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    # ------------------------ multi ------------------------
    # # multi threading
    # # print("------ multi thread -----", end="\n")
    # # with concurrent.futures.ThreadPoolExecutor(max_workers=len(nums)) as exec:
    # #     thread = list(exec.map(worker_thread, nums))

    # # multi process
    # # print("------ multi process -----", end="\n")
    # # with concurrent.futures.ProcessPoolExecutor(max_workers=len(nums)) as exec:
    # #     process = list(exec.map(worker_thread, nums))
