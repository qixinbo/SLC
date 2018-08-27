import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
r = requests.get(url)
print(r.status_code)
print(r.request.headers)