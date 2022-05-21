lst = [3, 1, 5, 2, 17, 45, 2324, 22, 4234, 444, 4554, 42323, 33, -12]

# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if lst[i] == lst[j]:
#             continue
#         elif lst[j] < lst[i]:
#             continue
#         elif lst[j] > lst[i]:
#             lst[i], lst[j] = lst[j], lst[i]
#
# print(lst)

for j in range(len(lst)):
    for j in range(len(lst) - 1 - j): # удаление последнего элемента который в каждой итерации оказывается самым большим, т.к. сравниваем всегда элемент с предыдущим элементом
        if lst[j] == lst[j + 1]:
            continue
        elif lst[j] < lst[j + 1]:
            continue
        elif lst[j] > lst[j + 1]:
            lst[j + 1], lst[j] = lst[j], lst[j + 1]

print(lst)
print(type(lst))

lst1 = set(lst)        # преобразование списка в множество, для того чтобы убрать повторяющиеся элементы
print(lst1)            # при этом множество неупорядоченно и элементы будут в бардаке, т.е убрал повторы - преобразовал обратно в список и сортируем
print(type(lst1))