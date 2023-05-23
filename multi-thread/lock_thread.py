import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s : %(message)s")


def worker_1(d, lock: threading.Lock):
    """ thread_1 job time -> 5"""
    logging.debug("start")

    # Lock Best Practice
    with lock:
        d["x"] += 10
        print(d)
        time.sleep(5)
        logging.debug("end")


def worker_2(d, lock: threading.Lock):
    """ thread_2 job time -> 2"""
    logging.debug("start")

    # Lock Worst Practice
    lock.acquire()
    d["x"] += 10
    print(d)
    lock.release()

    time.sleep(2)
    logging.debug("end")


# Lock
if __name__ == "__main__":
    d = {
        "x": 10
    }

    lock = threading.Lock()
    t1 = threading.Thread(target=worker_1, args=(d, lock))
    t2 = threading.Thread(target=worker_1, args=(d, lock))

    t1.start()
    t2.start()

    print(f"result >> {d}")
