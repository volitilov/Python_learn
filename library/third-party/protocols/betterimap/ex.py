import betterimap

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Распечатка последних 10 сообщений из почтового ящике, с вложениями
imap = betterimap.IMAPAdapter('volitilov@gmail.com', 'Kendar6709', 
    host='imap.gmail.com', ssl=True, port=993)
    
imap.select(imap.get_inbox_folder())
 
# Загрузка последних 10 сообщений
for msg in imap.search(limit=10):
    
    print(msg.subject)
    # prints unicode subject
    
#     print(msg.date)
#     # prints a timezone-aware datetime.datetime object
    
#     print(msg.from_addr)
#     # ('First Last', 'first.last@example.com')
    
#     print(msg.get_header('Date'))
#     # get any unicode header
    
#     print(msg.to)
#     # Prints receivers
    
#     # [
#     #    ('First Last2', 'first.last-2@example.com'),
#     #    ('First Last3', 'first.last-3@example.com'),
#     # ]
    
#     print(msg.html())
#     # распечатает html, if multipart
    
#     print(msg.plaintext())
#     # распечатает текс сообщения
    
              
#     for attachment in msg.attachments:
#         print(attachment.size) # integer
#         print(attachment.data) # the content of the attachment
#         print(attachment.filename) # unicode
#         print(attachment.content_type) # string




# # Ждёт пока появятся новые сообщения
# imap = betterimap.IMAPAdapter(
#     'username', 'password', host='imap.example.com', ssl=True)
# stop, stream = imap.idle(copy=False)
 
# for msg in stream:
#     print(msg)

# # Когда вы закончите, надо вызвать stop(), чтобы освободить ресурсы.    
# stop()





# # Поиск существующих сообщений
# imap = betterimap.IMAPAdapter(...)

# # поиск по теме сообщения
# for msg in email.easy_search(subject=u'Some subject'):
#     pass

# # поиск по дате
# for msg in email.easy_search(exact_date=datetime.date(2014, 9, 27)):
#     pass
        
# # поиск по периоду времени с, до 
# for msg in email.easy_search(since=datetime.date(2014, 9, 27)):
#     pass
# for msg in email.easy_search(before=datetime.date(2014, 9, 27), limit=10):
#     pass            
    
# # поиск по отправителю
# for msg in email.easy_search(sender='123@example.com', limit=5):
#     pass