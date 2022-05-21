a = [1, 3, 5, 7, 3, 8, 33, 2,]
counter = 0

for i in a:
    if i < 5:
        print(i, end=", ")

while counter < len(a):
    counter = a[counter]
    counter += 1
    if counter < 5:
        print(counter, end=", ")

