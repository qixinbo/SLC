import re

search = re.search(r'[1-9]\d{5}', 'BIT 100081')

# match object
print(search.group(0))
print(search.string)
print(search.re)
print(search.pos)
print(search.endpos)


match = re.match(r'[1-9]\d{5}', '100081 BIT')
if match:
	print(match.group(0))

findall = re.findall(r'[1-9]\d{5}', 'BIT100081 THU100084')
print(findall)

sp1 = re.split(r'[1-9]\d{5}', 'BIT100081 THU100084')
print(sp1)

sp2 = re.split(r'[1-9]\d{5}', 'BIT100081 THU100084', maxsplit = 1)
print(sp2)

for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 THU100084'):
	if m:
		print(m.group(0))

sub = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 THU100084')
print(sub)
