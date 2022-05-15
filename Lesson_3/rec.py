# def rec(n):
#     if n == 0:
#         return 1
#     else:
#         return n * rec(n - 1)



def rec(n):
   return 1 if n == 0 else n * rec(n - 1)
print(rec(5))
