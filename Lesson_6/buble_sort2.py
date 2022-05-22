a = [2, 5, 8, 2, -1, 6]

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]

print(a)

def rec(n):
    return 1 if n == 0 else n * rec(n - 1)

print(rec(5))
