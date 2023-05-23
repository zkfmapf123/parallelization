import concurrent.futures
import os
import subprocess
import time

COUNT = 10000000
LARGE_TEXT = "leedonggyu " * COUNT


def cpu_bounded():
    i = 0
    while i < COUNT:
        i = i + 1 - 2 + 3 - 4 + 5

    return "done"


def io_bounded(file_name: str):
    with open(file_name, "w+") as fs:
        fs.write(LARGE_TEXT)
        fs.seek(0)
        # fs.read()

    subprocess.run(["rm", "-rf", file_name], check=False)
    return "done"


def main():
    """
        io bounded 같은 경우 multi-threading이 효과적
        cpu bounded 같은 경우 multi-processing이 효과적
    """

    # io bounded (not multi-threading)
    start = time.time()
    io_bounded("test_1.txt")
    io_bounded("test_2.txt")
    print("io bounded time >> ", time.time() - start)

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exec:
        f1 = exec.submit(io_bounded, "test_1.txt")
        f2 = exec.submit(io_bounded, "test_2.txt")

        f1.result()
        f2.result()
    print("io bounded use multi-threading >> ", time.time() - start)

    # cpu bounded
    start = time.time()
    cpu_bounded()
    cpu_bounded()
    print("cpu bounded time >> ", time.time() - start)

    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as exec:
        f1 = exec.submit(cpu_bounded)
        f2 = exec.submit(cpu_bounded)

        f1.result()
        f2.result()
    print("cpu bounded use multi-process >> ", time.time() - start)


if __name__ == "__main__":
    main()
