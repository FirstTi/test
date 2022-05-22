

def decorator(some_func):
    def change(a, b):
        result = some_func(a, b)
        print(result * a)
        return result
    return change
   

@decorator
def changes(a, b):
    c = a + b
    return c


print(changes(4, 3))

# class Singleton():
#     @abstractmethod
#     def func():
#         pass
    
#     def __new__(cls):                               
#         if not hasattr(cls, 'instance'):            
#             cls.instance = super().__new__(cls)   
#         return cls.instance


