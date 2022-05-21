# for i in range(5):
#     print(i)
# for i in range(5):
#     print("It is possible!")
# for i in range(5):
#     print(i + 1)
group = ["Ilya", "Dima", "Pavel"]

for number, name in enumerate(group, 1):  # Дает каждому елементу в списке номер, нумерует объекты
    number = str(number)
    name = number + ")" + name.upper()
    print(name)
    name = name.lower()
    print(name)

print(group[0])
print(group[1])
print(group[2])
# print(group[3]) -- выдает ошибку т.к. выходим за пределы списка
