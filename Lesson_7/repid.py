def rec(n):
    return 1 if n == 0 else n * rec(n - 1)

print(rec(5))

a = [1, 3, 5, 2, -4]

for i in range(len(a)):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1],  a[j]

    print(a)

class Manager:

    def __enter__(self):
        print("open")

    #def body(self):           бесполезно, не выполняется
    #    print("Within")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close")


with Manager() as f:
    print(f)
    print("??This is body of with??")
    print(f)
