#!/usr/bin/python3

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import cgi, cgitb
import html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

cgitb.enable()

header = 'Content-Type: text/html\n\n'

form_html = '''
	<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8">
			<title>Friends CGI title</title>
		</head>
		<body>
			<h3>Friends list for: <i>NEW USER</i></h3>
			<form action="/cgi-bin/friend2.py">
				<b>Enter you Name:</b>
				<input type="hidden" name="action" value="edit">
				<input type="text" name="person" value="NEW USER" size="15">
				<p>
					<b>How many friends do you have?</b>
					{}
				</p>
				<button>Submit Query</button>
			</form>
		</body>
	</html>
'''

fradio = '<input type="radio" name="howmany" value="{}" {}>{}\n'



def show_form():
	friends = []
	for i in (0, 10, 20, 30, 50):
		checked = ''
		if i == 0:
			checked = 'checked'
		friends.append(fradio.format(str(i), checked, str(i)))
		res = form_html.format(''.join(friends))
	print('{}{}'.format(header, res))



res_html = '''
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


def do_results(who, howmany):
	print(header, res_html.format(who, who, howmany))



def _main():
	form = cgi.FieldStorage()

	if 'person' in form:
		who = html.escape(form['person'].value)
	else:
		who = 'NEW USER'

	if 'howmany' in form:
		howmany = form['howmany'].value
	else:
		howmany = 0


	if 'action' in form:
		do_results(who, howmany)
	else:
		show_form()



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	_main()
