import json
# from new_pizza import menu

# f = open("test.json", "w")
# a = json.dump(menu, f)
# f.close()

# f = open("test.json", "w")
# a = json.dump(menu, f)
# f.close()

menu = {
    'margarita': 400,
    'peperoni': 600,
}


f = open("test.json", "r")
a = json.load(f)
print(a)
print(type(a))
f.close()

# print(a)
# print(type(a))
# b = json.loads(a)
#
# print(b)
# print(type(b))
