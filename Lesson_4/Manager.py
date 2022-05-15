class Manager:

    def __enter__(self):
        def rec(n):
            return 1 if n == 0 else n * rec(n - 1)
        print("Открыли")
        return rec(5)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Закрыли")

with Manager() as f:
    print("Body of with")
    print(f)
