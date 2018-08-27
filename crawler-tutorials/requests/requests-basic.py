import requests

r = requests.get("http://www.baidu.com")
print(r.status_code) # 200 success, 404 failure 
print(r.text)
print(r.encoding) # Guess coding type from headers, if no "charset", then ISO-8859-1
print(r.apparent_encoding) # Guess coding type from the content
print(r.content)

# let "encoding=utf-8"
r.encoding = "utf-8"
print(r.text)

# Capture the error
print(r.raise_for_status())

# Operation of HTTP on resources: GET/HEAD/POST/PUT/PATCH/DELETE
# Patch -> modify local; PUT -> cover the original 

# Parameters of requests.request():
# params: dict or byte sequence
# data: as the request's content
# json: request's content
# headers: dict, 
# cookies:
# files:
# timeout: unit is second
# proxies: proxy server

# Pay attentions to the robots.txt. We can adopt the way to similar to HUMAN BEHAVIOR.