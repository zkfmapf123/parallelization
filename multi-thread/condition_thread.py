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


def worker_1(c: threading.Condition,):

    with c:
        c.wait()
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


def worker_2(c: threading.Condition,):

    with c:
        c.wait()
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


def worker_3(c: threading.Condition,):
    with c:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")
        c.notify_all()


if __name__ == "__main__":
    """
        t1 -> t2 -> t3 (실행흐름)
        t3 (condition)

        t3 -> t1 -> t2 흐름으로 동작
    """
    c = threading.Condition()

    t1 = threading.Thread(target=worker_1, args=(c,))
    t2 = threading.Thread(target=worker_2, args=(c,))
    t3 = threading.Thread(target=worker_3, args=(c,))

    for t in (t1, t2, t3):
        t.start()
