import requests

url = "http://ip138.com/ips138.asp?ip="
r = requests.get(url + '202.204.80.112')
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.text)