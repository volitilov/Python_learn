from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = 'ACbaadea46980cc4a045d509683159825e'
# Your Auth Token from twilio.com/console
auth_token  = '7db4a54d901eeb4522e3e048e3f90810'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to='+375336157799', 
    from_='+19093230273',
    body="Hello from Pythman!")

print(message.sid)