import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s : %(message)s")


def worker_1(lock: threading.Lock):
    """ thread_1 job time -> 5"""

    # Lock Best Practice
    with lock:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


def worker_2(lock: threading.Lock):
    """ thread_2 job time -> 5"""

    # Lock Best Practice
    with lock:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


def worker_3(lock: threading.Lock):
    """ thread_3 job time -> 5"""

    # Lock Best Practice
    with lock:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


def worker_4(lock: threading.Lock):
    """ thread_4 job time -> 5"""

    # Lock Best Practice
    with lock:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


# Lock
if __name__ == "__main__":
    """
        threading.Semaphore(n):
            n만큼 실행할 스레드를 결정함
    """
    semaphore = threading.Semaphore(2)

    t1 = threading.Thread(target=worker_1, args=(semaphore,))
    t2 = threading.Thread(target=worker_2, args=(semaphore,))
    t3 = threading.Thread(target=worker_3, args=(semaphore,))
    t4 = threading.Thread(target=worker_4, args=(semaphore,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
