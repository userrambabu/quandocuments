from twilio.rest import Client

account_sid='AC1514e34b0a7b6560570fa7f0b325284d'
auth_token='616a50ab26a3dd33dee2db248d78ed08'

to_number='+918148192114'
from_number='+14027808647'

client=Client(account_sid,auth_token)
call=client.calls.create(
    twiml='<Response><Say>welcome ,done using python code</Say></Response>',
    to=to_number,
    from_=from_number,
    )
print(call.sid)
