import logging
import multiprocessing
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(processName)s >> %(message)s"
)


def user_input(l: list[int], d: dict,  n):
    l.reverse()

    d["x"] += 1.0
    n.y += 1.0


if __name__ == "__main__":
    """
        Manager:
            subprocess 관리
            Server 와 Client간의 데이터 관리 

        Props:
            Value와 Array보다는 Pyhton 스러운 기능
        Cons:
            속도가 느리다
    """

    with multiprocessing.Manager() as manager:
        l = manager.list()
        d = manager.dict()
        n = manager.Namespace()

        l.append([1, 2, 3])
        d["x"] = 10
        n.y = 3.14

        for _ in range(3):
            p = multiprocessing.Process(target=user_input, args=(l, d, n))
            p.start()
            p.join()

    logging.debug(l)
    logging.debug(d)
    logging.debug(n)
