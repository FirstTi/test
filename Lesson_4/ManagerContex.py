class ManagerContex:

    def __enter__(self):
        print("Отработал enter")
        return 13

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Отработал exit")


with ManagerContex() as f:
    print("Body of with")
    print(f)
