from ftplib import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	with FTP('ftp1.at.proftpd.org') as ftp:
		print(ftp.login())
		print(ftp.getwelcome())
		print(ftp.dir())