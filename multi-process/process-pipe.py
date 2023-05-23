import logging
import multiprocessing
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(processName)s >> %(message)s"
)


def user_input(conn):
    conn.send(["test"])
    time.sleep(5)
    conn.close()


if __name__ == "__main__":

    """
        multiprocessing.Process:
            A Process의 결과를 B Process에서 실행
    """

    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=user_input, args=(parent_conn,))
    p.start()
    # p.join()  # 5초 뒤에 출력
    logging.debug(f"child_process >> {child_conn.recv()}")
