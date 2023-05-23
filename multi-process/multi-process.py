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
    time.sleep(10)
    logging.debug("end")


def worker_thread_2(num: int) -> None:
    logging.debug('start')
    print(num)
    logging.debug("end")


if __name__ == "__main__":
    """
        execute flow:

        t1(start) -> t2(start) -> t1(end) -> t2(end)
    """
    i = 10

    t1 = multiprocessing.Process(target=worker_thread_1, args=(i,))
    t1.daemon = True
    t2 = multiprocessing.Process(target=worker_thread_2,
                                 name="unknown_process", args=(i,))

    for t in (t1, t2):
        t.start()
        t.join()  # twait until exit
