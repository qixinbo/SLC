import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
print(demo)

# bs4's HTML parser & lxml's HTML parser & lxml's XML parser & html5lib's parser
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())

# HTML Document = Tag Tree = BeautifulSoup Class
print(soup.a)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.attrs)
print(soup.a.string)
print(type(soup.a.attrs))
