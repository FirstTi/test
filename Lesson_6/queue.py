class Queue:                        # структура данных - Очередь
    def __init__(self, data):
        self.queue_data = data

    def add(self, element):
        self.queue_data.append(element)
    
    def get(self):
        return self.queue_data.pop(0)


queue = Queue([1, 2, 3])
queue.add(7)

print(queue.queue_data)
print(queue.get())              # получаем первый и только первый элемент из очереди, и удаляем его
print(queue.queue_data)

