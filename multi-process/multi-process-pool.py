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
    # async (비동기)
    # with multiprocessing.Pool(5) as p:

    #     for _ in range(10):
    #         process1 = p.apply_async(worker_thread_1, (100,))
    #         procees2 = p.apply_async(worker_thread_1, (100,))
    #         logging.debug("executed...")
    #         logging.debug(process1.get(), procees2.get())

    # sync (동기)
    with multiprocessing.Pool(5) as p:

        for _ in range(10):
            process1 = p.apply(worker_thread_1, (100,))
            process2 = p.apply(worker_thread_1, (100,))
            logging.debug("executed apply...")
            logging.debug(process1, process2)
