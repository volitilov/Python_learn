from ftplib import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# ftps = FTP('ftp.pureftpd.org')




# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	with FTP_TLS('ftp.pureftpd.org') as ftps:
		print(ftps.login())
		print(ftps.prot_p())