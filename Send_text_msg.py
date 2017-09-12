# -*- coding: cp1252 -*-
from twilio.rest import Client

# id do twilio
account_sid = "AC0cc7782eb8a37b9b293669a0fae9f4bb"
#  Auth Token 
auth_token  = "10d966feb35a27589bf7fdf52ee6fe64"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5543998625629", 
    from_="+1215-703-2881",
    body="Ola , esse eh um teste de sms!")

print(message.sid)
