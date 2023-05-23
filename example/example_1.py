"""
    1초 간격으로 1~10까지 숫자를 생성
"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format=("%(message)s")
)


def worker_thread(num_dict: dict):
    time.sleep(1)
    logging.debug(num_dict["x"])
    num_dict["x"] += 1


def main():
    num_dict = {
        "x": 1
    }

    # 1 ~ 10
    for _ in range(10):
        thread = threading.Thread(target=worker_thread, args=(num_dict,))
        thread.start()
        thread.join()


if __name__ == "__main__":
    main()
