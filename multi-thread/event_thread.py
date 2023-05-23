import logging
import threading
import time

""" 
    event.set() 한 스레드가 먼저 실행 -> 종료된 후 
    event.wait() 한 스레드들이 실행 -> 종료된다
"""

logging.basicConfig(
    level=logging.DEBUG, format="%(threadName)s: %(message)s"
)


def worker_1(e: threading.Event,):

    e.wait()
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")


def worker_2(e: threading.Event,):

    e.wait()
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def worker_3(e: threading.Event,):

    logging.debug("start")
    time.sleep(3)
    logging.debug("end")
    e.set()


if __name__ == "__main__":
    """
        event.set()을 한 스레드가 먼저 실행 된 후에 
        event.wait() 스레드들이 나중에 실행 됨
    """
    e = threading.Event()
    t1 = threading.Thread(target=worker_1, args=(e,))
    t2 = threading.Thread(target=worker_2, args=(e,))
    t3 = threading.Thread(target=worker_3, args=(e,))

    for t in (t1, t2, t3):
        t.start()
