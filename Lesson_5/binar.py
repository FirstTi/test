lst = [1, 2, 3, 5, 7]

find = 3

def rec(lst, find):
    left_index = 0
    right_index = len(lst) - 1
    midle_index = len(lst) // 2

    if find < lst[midle_index]:
        right_index = midle_index
        lst = lst[:right_index]
        rec(lst, find)
    elif find > lst[midle_index]:
        left_index = midle_index
        lst = lst[left_index:]
        rec(lst, find)
    elif find == lst[midle_index]:
        print(f"Искали {find} и нашли")
    else:
        print("Нет такого элемента")

rec(lst, find)





