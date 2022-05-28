import requests

r = requests.get("https://apieasycall.pt1.ru", verify=False)


print(r.text)
