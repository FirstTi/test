f = [2, -3, 5, 2.4, 8, -4]
d = [4, -5, 3, 5, -7, 3]

for i in range(len(f)):
    for j in range(len(f) - 1 - i):
        if f[j] > f[j + 1]:
            f[j], f[j + 1] = f[j + 1], f[j]

print(f)

class Manager:

    def __enter__(self):
        def rec(n):
            return 1 if n == 0 else n * rec(n - 1)
        return rec(5)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close")

with Manager() as f:
    print(f)
    print("body")

def smallest(d):
    small = d[0]
    for i in range(len(d) - 1):
        if small > d[i]:
            small = d[i]
    return small

def sort(d):
    d1 = []
    for i in range(len(d)):
        a = smallest(d)  # создал переменную с вызовом функции чтобы не писать ее два раза - на append и remove
        d1.append(a)  # запускаем предыдущую функцию в кот. находим наименьший и добавляем его в новосозданный список
        d.remove(a)
    return d1

print(d)
print(sort(d))
