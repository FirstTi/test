from threading import Thread, Lock

counter = 0

lock = Lock()


def func():
    lock.acquier()
    global counter
    f = counter
    counter = f + 1
    lock.release()


print(f"Счетчик равен {counter}")
