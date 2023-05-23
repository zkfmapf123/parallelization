import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s : %(message)s")


def worker_1():
    """ thread_1 """
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def worker_2(x, y):
    """ thread_2 """
    logging.debug("start")
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug("end")


def worker_3():
    """ thread_3 """
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


if __name__ == "__main__":
    t1 = threading.Thread(name="rename worker1", target=worker_1)
    t2 = threading.Thread(target=worker_2, args=(100,), kwargs={"y": 200})
    t3 = threading.Thread(target=worker_3)

    t1.start()
    t2.start()
    t3.start()
    print("-----processing-----")
