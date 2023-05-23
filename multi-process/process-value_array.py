import logging
import multiprocessing
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(processName)s >> %(message)s"
)


def user_input(num: float, arr: list[int]):

    logging.debug(num)
    num.value += 1.0

    logging.debug(arr)
    for i, _ in enumerate(arr):
        arr[i] *= 2


if __name__ == "__main__":
    """
        Value, Array:
            프로세스간의 공유메모리
    """

    num = multiprocessing.Value("f", 3.14)
    arr = multiprocessing.Array("i", [i for i in range(10)])

    for _ in range(2):
        p = multiprocessing.Process(target=user_input, args=(num, arr))
        p.start()
        p.join()

    logging.debug(num.value)
    logging.debug(arr[:])
