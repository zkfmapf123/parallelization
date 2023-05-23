import logging
import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    level=logging.DEBUG, format="%(threadName)s >> %(message)s"
)


def worker_thread_fn(a, b):
    logging.debug("start")

    r = a*b
    logging.debug(r)
    logging.debug("end")
    return r


def main():
    with ThreadPoolExecutor(max_workers=10) as exec:
        for _ in range(3):
            thread = exec.submit(worker_thread_fn, 2, 5)
            logging.debug(thread.result)


if __name__ == "__main__":
    main()
