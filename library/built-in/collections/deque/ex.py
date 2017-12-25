from collections import deque

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

d = deque()
obj = {}
obj['xxx'] = ['bob', 'sam', 'ana']
d += obj
while d:
	first_name = d.popleft()
	last_name = d.pop()

