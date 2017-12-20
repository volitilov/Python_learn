import re

source = 'You and you'
a = re.match('You', source)
b = re.match('you', source)

if a: print(a.group())	# You
if b: print(b.group())	# None

b = re.search('you', source)
if b: print(b.group())	# you

c = re.findall('o.', source)
print(c) 	# ['ou', 'ou']

d = re.split(' ', source)
print(d)	# ['You', 'and', 'you']

g = re.sub(' ', '_', source)
print(g)	# You_and_you

