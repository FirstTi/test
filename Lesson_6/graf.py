class Queue:                        # структура данных - Очередь
    def __init__(self, data):
        self.queue_data = data

    def add(self, element):
        self.queue_data.append(element)
    
    def get(self):
        return self.queue_data.pop(0)


queue = Queue([])

graph = {                      # структура данных граф и алгоритм поиска в ширину по графу 
    "A": ["B", "E"],
    "B": ["A", "C", "D"],
    "C": ["B", "D", "K"],
    "D": ["B", "C"],
    "E": ["A", "K"],
    "K": ["E", "C"]
}

def width_search(graph, start):        # прохождение по всему графу
    visited = []
    visited.append(start)
    queue.add(start)
    while queue.queue_data:
        top_element = queue.get()      # текущая вершина, начинаем путь отсюда при первой итерации
        tops = graph[top_element]              # список смежных вершин
        for i in tops:
            if i not in visited:            
                visited.append(i)       # добавление посещенной вершины в список     
                queue.add(i)            # переназначение переменной старт
    return visited


print(width_search(graph, "A"))

def show_my_the_way(graph, start, finish):    # поиск кратчайшего пути    
    visited = []
    visited.append(start)
    queue.add(start)
    while queue.queue_data:
        top_element = queue.get()      # текущая вершина, начинаем путь отсюда при первой итерации
        tops = graph[top_element]              # список смежных вершин
        for i in tops:
            if i == finish:
                break
            if i not in visited:
                visited.append(i)
                queue.add(i)
    
    for i in visited:
        if start in graph[i] and finish in graph[i]:
            path = i

    return path

# visited = width_search(graph, "A", "D")
print(show_my_the_way(graph, "A", "K"))
print(show_my_the_way(graph, "A", "D"))


