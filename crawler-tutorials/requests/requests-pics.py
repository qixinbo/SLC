import requests
import os

url = "http://image.ngchina.com.cn/2018/0824/20180824031639239.jpg"
root = "/home/qixinbo/temp/"
path = root + url.split('/')[-1]
print(path)

try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			print("Picture saved successfully")
	else:
		print("Picture existed")
except:
	print("Crawling failure")