#!/usr/bin/python3

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from atexit import register
import cgi, cgitb
import html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def _main():
	reshtml = '''Content-Type: text/html\n
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="utf-8">
				<title>Friends CGI title</title>
			</head>
			<body>
				<h3>Friends list for: <i>{}</i></h3>
				<p>Your name is: <b>{}</b></p>
				<p>Your have: <b>{}</b> friends.</p>
			</body>
		</html>
	'''

	cgitb.enable()
	form = cgi.FieldStorage()
	who = html.escape(form['person'].value)
	howmany = form['howmany'].value
	print(reshtml.format(who, who, howmany))
	

@register
def _atexit(): pass



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
