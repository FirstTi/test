from flask import Flask, render_template, abort, request
from bs4 import BeautifulSoup
from pizza_OOP import pizzeria
import json

app = Flask(__name__)


@app.route("/")
def hell():
    return "Welcome"


@app.route("/pizzeria/menu", methods=["GET"])
def get_menu():
    menu = pizzeria.load_menu()
    pizza_name = request.args.get("pizza_name")
    if pizza_name:  # если клиенты задали параметр имя пиццы то вернет ее стоимость
        if pizza_name in menu.keys():
            return json.dumps({pizza_name: menu[pizza_name]})
        else:
            abort(404)
    else:
        result = json.dumps(menu)
        return result


@app.route("/pizzeria/menu/pizza", methods=["POST"])
def add_pizza():
    data = request.form
    pizza_name = data.get("name")
    pizza_cost = data.get("cost")
    pizzeria.add_pizza(pizza_name, pizza_cost)
    return '', 201


@app.route("/pizzeria/menu/pizza", methods=["DELETE"])
def remove_pizza():
    pizza_name = request.args.get("pizza_name")
    pizzeria.remove_pizza(pizza_name)
    return '', 204


@app.route("/pizzeria/order", methods=["POST"])
def order_pizza():
    data = request.form
    order = data.getlist("order")
    print(order)
    result = pizzeria.order_pizza_api(order)
    if result:
        return json.dumps({"cost": result})
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
