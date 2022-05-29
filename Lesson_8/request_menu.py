import requests

menu = requests.get("http://127.0.0.1:5000/pizzeria/menu")
print(menu.json())

menu = requests.get("http://127.0.0.1:5000/pizzeria/menu", params={"pizza_name": "margarita"})
print(menu.json())

menu = requests.get("http://127.0.0.1:5000/pizzeria/menu", params={"pizza_name": "NotInMenu"})
print(menu.status_code)
if menu.status_code != 404:
    print(menu.json())
else:
    print("Pizza Without menu")

menu = requests.get("http://127.0.0.1:5000/pizzeria/menu", params={"pizza_name": "Peper"})
print(menu.json())
