import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+12284600437'

myCellPhone = '+12108070139'

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body="Hi there!")

print(textmessage.status)

#make a phone call 

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
                                    to=myCellPhone,from_=TwilioNumber) 