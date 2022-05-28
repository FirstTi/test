import time
from threading import Thread

# class MyThread(Thread):
#     def start(self):
#         print("start")


def start_rocket(id):
    time.sleep(3)
    print(f"Ракета с id {id} запущена")
    #return id + 1 чтобы убрать None нужно добавить return

threads_list= []

# for i in range(1, 6):
#     print(start_rocket(i)) # или убрать print и просто запустить функцию

for i in range(5):
    thread_objekt = Thread(target=start_rocket, args=(i, ))
    threads_list.append(thread_objekt)

for i in threads_list:
    i.start()

for i in threads_list:
    i.join()
