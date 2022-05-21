# Бинарный поиск
# с помощью бинарного поиска найти елемент 7

find = 7
search_list = [5, 7, 10, 11, 12, 16] # можно и с кортежем


def recorsive_binar_search(search_list, find):
    left_index = 0
    right_index = len(search_list) - 1
    median_index = len(search_list) // 2           # находим центральный элемент списка по индексу посредством целочисленного деления
    if find < search_list[median_index]:
        right_index = median_index                 # назначаем крайнему правому индексу значение среднего элемента
        search_list = search_list[:right_index]    # назначаем списку новое значение, начиная с правого индекса(с помощью среза списка), который равен среднему индексу
        recorsive_binar_search(search_list, find)
    elif find > search_list[median_index]:         # список обращается по индексу и достает элемент, который и сравнивается с find
        left_index = median_index
        search_list = search_list[left_index:]
        recorsive_binar_search(search_list, find)
    elif find == search_list[median_index]:
        print(search_list[median_index])
        print("Найдено")

try:
    recorsive_binar_search(search_list=search_list, find=7)  # исключение ошибки, попытка поиска элемента которого нет в списке
except IndexError:
    print("Нет элемента в списке")







