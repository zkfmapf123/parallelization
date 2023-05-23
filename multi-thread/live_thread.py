import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s : %(message)s")


def worker_1():
    """ thread_1 job time -> 5"""
    logging.debug("start")
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
        threading.enumerate():
            현재 run 상태인 Thread
    """
    # threads = []
    for _ in range(0, 5):
        t = threading.Thread(target=worker_1)
        t.daemon = True

        t.start()
        # threads.append(t)

    for thread in threading.enumerate():
        if thread is threading.current_thread():
            print(thread)
            continue

        thread.join()
