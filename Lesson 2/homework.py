a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
counter = 0

for i in a:
    if i < 5:
        print(i)

while counter in range(len(a)):
    i = a[counter]
    if i < 5:
        print(i)
    counter += 1
