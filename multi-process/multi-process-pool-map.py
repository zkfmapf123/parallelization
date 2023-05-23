import logging
import multiprocessing
import time
from multiprocessing import (Array, Barrier, Condition, Event, Lock, Manager,
                             Pipe, Process, Queue, RLock, Semaphore, Value)

logging.basicConfig(
    level=logging.DEBUG, format="%(processName)s >> %(message)s"
)


def worker_thread_1(num: int) -> None:
    logging.debug('start')
    print(num)
    time.sleep(3)
    logging.debug("end")
    return num


# def worker_thread_2(num: int) -> None:
#     logging.debug('start')
#     print(num)
#     logging.debug("end")


if __name__ == "__main__":
    """
        processPool in 5
    """

    i = 100
    """
        map을 활용해서 동기적으로 운용
    """
    # sync_map (동기)
    # with multiprocessing.Pool(5) as p:

    #     for _ in range(10):
    #         ps = p.map(worker_thread_1, [100, 100, 100])  # Parallelization
    #         logging.debug(f"executed... {len(ps)}")
    #         logging.debug(ps)

    """
        map_async 을 활용해서 비동기적으로 운용
    """
    # async_map (비동기)
    # with multiprocessing.Pool(5) as p:

    #     for _ in range(10):
    #         # Parallelization
    #         ps = p.map_async(worker_thread_1, [100, 100, 100])
    #         # logging.debug(f"executed... {len(ps)}")
    #         logging.debug(ps.get())

    """
        use Iterator
    """
    with multiprocessing.Pool(5) as p:

        for _ in range(10):
            # Parallelization
            ps = p.imap(worker_thread_1, [100, 100, 100])
            # logging.debug(f"executed... {len(ps)}")
            for p in ps:
                logging.debug(p)
