find = 577
search_list = [1, 4, 6, 12, 35, 577]

left = 0
right = len(search_list) - 1
counter = 0
last = right


if find == search_list[last]:
    print(find)
else:
    while left <= right:
        counter += 1
        median = (left + right) // 2
        if search_list[median] == find:
            print(find)
            print(counter)
            break

        elif find < search_list[median]:
            right = median

        elif find > search_list[median]:
            left = median

