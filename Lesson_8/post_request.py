import requests

r = requests.post("http://127.0.0.1:5000/pizzeria/menu/pizza", data={"name": "Peper", "cost": 600})
print(r.status_code)
