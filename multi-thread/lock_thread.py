import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(threadName)s >> %(message)s"
)


def worker_thread_1(d, lock):

    with lock:
        time.sleep(2)
        d["x"] += 10
        logging.debug(d)


def worker_thread_2(d, lock):

    with lock:
        time.sleep(5)
        d["x"] += 20
        logging.debug(d)


if __name__ == "__main__":
    """
        execution flow:
            worker_thread_1 -> worker_thread_2
    """

    d = {"x": 0}
    lock = threading.Lock()

    threads = []
    for worker in (worker_thread_1, worker_thread_2):
        t = threading.Thread(target=worker, args=(d, lock,))
        t.start()
        t.join()
        threads.append(t)
