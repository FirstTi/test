a = [1, 13, 1, 2, 3, 5, 8, 13, 21, 21, 55, 89]
b = []
c = 0

for c in range(len(a)):
    i = a[c]
    if i != c:
        b.append(i)
    else:
        continue
    c += 1
print(b)


