a = [1, 13, 1, 2, 3, 5, 8, 13, 21, 21, 55, 89]

for i in a:
    for j in a:
        if i > j:
            i = i
        else:
            i = j
print(i)
# lst = [1, 13, 1, 2, 3, 5, 8, 13, 21, 21, 55, 89]
# a = 0
#
# for i in lst:
#     if i > a:
#         i = i
#     elif i < a:
#         i = a
# print(i)
