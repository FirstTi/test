list_1 = [1, 2, 3, 4, 4]
tuple_1 = (1, 2, 3, 4)
mnojestvo = {1, 2, 3, 4}


b = set(list_1)
print(type(list_1))
print(type(b))
print(list_1)
print(b)

dict1 = {
        (1, 2, 3, 4): "fhyudyh",
        "dict_login": "12345",
        'Ivan': 'jghiur',
        'Sanya': 'hgds'
        }
print(dict1['dict_login'])
print(dict1["Ivan"])
print(dict1["Sanya"])

print(dict1.keys())
print(dict1.values())

print(list(dict1.values())[0])
