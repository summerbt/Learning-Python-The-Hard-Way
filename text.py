##Text Message
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# put your own credentials here 
ACCOUNT_SID = "ACecb95f119818d47b612d524e78c6c36b" 
AUTH_TOKEN = "7badece27ccddb87e4fec414b1c2a243" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="4144035693", 
	from_="4148778688", 
	body="Hey there, I'm sending this from my python program. - Summer",  
)
phone_dict={"Di":4147596556,"Catherine":7606834858,"Mom":4149407930,"Dad":4144262873,"Me":4144035693}

for k,v in phone_dict.iteritems():
	client.messages.create(
	to=v, 
	from_="4148778688", 
	body="Hey there %s, I'm sending this from my python program. - Summer" % k,  
)