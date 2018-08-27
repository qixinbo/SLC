import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, "html.parser")
#print(soup.prettify())

# downwards loop
print(soup.body.contents)
print(soup.body.contents[1])

# upwards loop
print(soup.title.parent)
for parent in soup.a.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)

# parallel loop
print(soup.a.next_sibling)
print(soup.a.previous_sibling)