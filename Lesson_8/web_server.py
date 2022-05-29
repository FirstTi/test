from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests



app = Flask(__name__)

@app.route("/")
def hell():
    first = "<p>Welcome to hell!</p>" #
    second = "<p><a href='http://127.0.1:5001/next_page'>Следующая страница</a></p>" #
    third = "<a href='http://127.0.0.1:5001/weather'>Температура сегодня</a>" #
    forth = "<a href='http://127.0.0.1:5001/>"
    return first + second + third + forth

@app.route("/weather")
def weather():
    page = requests.get("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%" #
                        "D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0" #
                        "%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5" #
                        )

    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find("div", {"id": "ArchTemp"}).find("span", {"class": "t_0"})
    return result.text

@app.route("/next_page")
def next_page():
    return render_template('index.html') #






if __name__ == "__main__":
    app.run(debug=True, port=5001)
