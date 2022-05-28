from multiprocessing import Process
import os
from time import sleep


def func(start, end, timeout):
    while start < end:
        print(f"Precess {os.getpid()}: {start}")
        start += 1
        sleep(timeout)

if __name__ == "__main__":
    process1 = Process(target=func, args=(3, 10, 1))
    process2 = Process(target=func, args=(5, 20, 0.5))
    process1.start()
    process2.start()

    print("End")

