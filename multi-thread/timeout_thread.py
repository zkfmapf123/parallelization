import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s : %(message)s")


def worker_1(**kwargs):
    """ thread_1 job time -> 5"""
    logging.debug("start")
    print(kwargs)
    time.sleep(5)
    logging.debug("end")


def worker_2():
    """ thread_2 job time -> 2"""
    logging.debug("start")
    time.sleep(2)
    logging.debug("end")


def worker_3():
    """ thread_3 job time -> 2"""
    logging.debug("start")
    time.sleep(2)
    logging.debug("end")


if __name__ == "__main__":
    """
        threading.Timer:
            call after 3 seconds
    """
    t = threading.Timer(3, worker_1, kwargs={"y": 100})

    t.start()
