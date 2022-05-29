import requests

menu = requests.get("http://127.0.0.1:5000/pizzeria/menu")
print(menu.json())

r = requests.delete("http://127.0.0.1:5000/pizzeria/menu/pizza", params={"pizza_name": "Peper"})
print(r.status_code)

menu = requests.get("http://127.0.0.1:5000/pizzeria/menu")
print(menu.json())
