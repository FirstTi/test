from bs4 import BeautifulSoup
import requests

page = requests.get('http://127.0.0.1:5000/next_page')
soup = BeautifulSoup(page.text, "html.parser")
result = soup.find_all("div")
result2 = soup.find("body").find("div", {"id": "1"})


print(page.text)
print(result)
print(result2)

for i in result:
    print(i.text)
