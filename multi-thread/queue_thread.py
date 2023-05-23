import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format="%(threadName)s: %(message)s"
)


def worker_1(q: queue):
    logging.debug("start")

    while True:
        item = q.get()
        if item is None:
            break

        logging.debug(item)
        q.task_done()

    logging.debug("end")


def worker_2(q):
    logging.debug("start")
    logging.debug(q.get())
    logging.debug(q.get())  # Queue 자체가 Lock이 자동적으로 걸리게된다
    logging.debug("end")


# Single Thread Task use Queue
# if __name__ == "__main__":
#     q = queue.Queue()

#     for i in range(0, 10):
#         q.put(i)

#     t1 = threading.Thread(target=worker_1, args=(q,))
#     t1.start()

#     logging.debug("tasks are not done")
#     q.join()
#     logging.debug("tasks are done")
#     q.put(None)

#     t1.join()

# Multi Thread Task use Queue (3)
if __name__ == "__main__":
    q = queue.Queue()

    for i in range(0, 100000):
        q.put(i)

    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker_1, args=(q,))
        t.start()
        ts.append(t)

    logging.debug("tasks are not done!!")
    q.join()
    logging.debug('tasks are done')

    for _ in range(len(ts)):
        q.put(None)

    for t in ts:
        t.join()
