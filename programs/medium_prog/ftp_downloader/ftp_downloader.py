#!/usr/bin/python3

# Эга программа используется для загрузки файлов из интернета
# по протоколу ftp

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import ftplib
import os
import socket

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

HOST = 'ftp.byfly.by'
DIRN = 'ubuntu'
FILE = 'ls-lR.gz'


def main():
	try:
		f = ftplib.FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print('ERROR: canot reach "{}"'.format(HOST))
		return
	print('*** Connected to host "{}"'.format(HOST))

	try:
		f.login()
	except ftplib.error_perm:
		print('ERROR: canot login anonymously')
		f.quit()
		return
	print('*** Logged in as "anonymous"')

	try:
		f.cwd(DIRN)
	except ftplib.error_perm:
		print('ERROR: canot CD to "{}" folder'.format(DIRN))
		f.quit()
		return
	print('*** Changed to "{}" folder'.format(DIRN))

	try:
		loc = open(FILE, 'wb')
		f.retrbinary('RETR {}'.format(FILE), loc.write)
		loc.close()
	except ftplib.error_perm:
		print('ERROR: canot read file "{}" to CWD'.format(FILE))
		os.unlink(FILE)
	else:
		print('*** Downloaded "{}" to CWD'.format(FILE))

	f.quit()
	return


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	main()