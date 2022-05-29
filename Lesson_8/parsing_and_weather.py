from bs4 import BeautifulSoup
import requests

page = requests.get("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%"
                    "D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0"
                    "%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5"
                    )

soup = BeautifulSoup(page.text, "html.parser")
result = soup.find("div", {"id": "ArchTemp"}).find("span", {"class": "t_0"})

print(result)
print(result.text)
