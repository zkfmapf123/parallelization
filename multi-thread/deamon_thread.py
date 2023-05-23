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
        daemon : 
            작업을 기다리지 않고 종료

        join :
            작업을 기다림
    """
    t1 = threading.Thread(target=worker_1)
    t1.daemon = True

    t2 = threading.Thread(target=worker_2)
    t3 = threading.Thread(target=worker_3)

    t1.start()
    t2.start()
    t3.start()

    # Required (좀비 프로세스가 발생할 우려가 존재함)
    t1.join()
    t2.join()
    print("-----processing-----")
