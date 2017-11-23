from collections import deque

d = deque()
obj = {}
obj['xxx'] = ['bob', 'sam', 'ana']
obj['bob'] = ['xxx', 'sam', 'ana']
obj['sam'] = []
obj['ana'] = []


d += obj

searched = []

while d:
	name = d.popleft()
	if not name in searched:
		searched.append(name)
		d += obj[name]

for n in searched:
	print(n)
