class MyOwnException(Exception):
    pass


try:
    raise MyOwnException
except MyOwnException:
    print("Обработал")
