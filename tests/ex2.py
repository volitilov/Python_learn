import re, os

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with os.popen('who', 'r') as f:
	for each_line in f:
		print(re.split(r'\s\s+|\t', each_line.rstrip()))
		# ['py', 'tty7', '2018-01-22 19:08 (:0)']
