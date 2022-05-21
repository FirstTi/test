class Manager():
    def __enter__(self):
        print("Open")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Close")


with Manager() as f:

    print(f)
