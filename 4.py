from twilio.rest import Client

account_sid='AC1514e34b0a7b6560570fa7f0b325284d'
auth_token='616a50ab26a3dd33dee2db248d78ed08'

client=Client(account_sid,auth_token)
message=client.messages.create(
    from_='+14027808647',
    body='Hi,how are you',
    to='+918148192114'
    )
print(message.sid)
