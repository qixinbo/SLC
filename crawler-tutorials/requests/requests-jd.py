import requests
url = "http://item.jd.com/7348367.html"
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("Failure")