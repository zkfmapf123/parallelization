import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format="%(threadName)s >> %(message)s"
)


def worker_thread_1(barrier: threading.Barrier):
    """
        현재 Barrier 가 2개니까 
        wait을 함으로써 1개가 -- (1)
    """
    r = barrier.wait()
    logging.debug(f"num={r}")

    while True:
        logging.debug("start")
        time.sleep(2)
        logging.debug("end")


def worker_thread_2(barrier: threading.Barrier):
    """
        현재 Barrier 가 2개니까 
        wait을 함으로써 1개가 -- (0)
    """

    r = barrier.wait()
    logging.debug(f"num={r}")

    while True:
        logging.debug("start")
        time.sleep(2)
        logging.debug("end")


def worker_thread_3(cond: threading.Barrier):

    r = barrier.wait()
    logging.debug(f"num={r}")

    while True:
        logging.debug("start")
        time.sleep(2)
        logging.debug("end")


if __name__ == "__main__":
    """
        Barrier:
            정해진 Thread개수만큼 실행하고 정지

        Thread가 3개가 구동이 되지만 Barrier(2) 개만 실행됨
    """
    barrier = threading.Barrier(2)

    threads = []
    for worker in (worker_thread_1, worker_thread_2, worker_thread_3):
        thread = threading.Thread(target=worker, args=(barrier, ))
        thread.start()
        threads.append(thread)

    print("active count >> ", threading.active_count())
