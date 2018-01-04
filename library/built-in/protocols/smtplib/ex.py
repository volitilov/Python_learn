import smtplib
from email.mime.text import MIMEText

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
print('Autorization gmail:')
MAIL_USERNAME = input('username: ')
MAIL_PASSWORD = input('password: ')
msg = input('message: ')
msg = MIMEText('\n {}'.format(msg).encode('utf-8'), _charset='utf-8')
 
smtpObj = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)
smtpObj.ehlo()
smtpObj.login(MAIL_USERNAME, MAIL_PASSWORD)

smtpObj.sendmail('volitilov@gmail.com', 'otivito@mail.ru', 
    'Subject: xxx-pythman-xxx. \n{}'.format(msg))
smtpObj.quit()