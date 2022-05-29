import requests

cost = requests.post("http://127.0.0.1:5000/pizzeria/order", data={"order": ["margarita", "peperoni"]})
print(cost.status_code)
print(cost.json())
