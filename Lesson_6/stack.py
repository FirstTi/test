class Stack:
    def __init__(self, data):               # структура данных - Стек
        self.stack_data = data

    def add(self, element):
        self.stack_data.append(element)

    def get(self):
        return self.stack_data.pop(-1)


stack = Stack([1, 2, 4])

stack.add(6)
print(stack.stack_data)
print(stack.get())
