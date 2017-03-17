# we import the Twilio client from the dependency we just installed
from twilio.rest import TwilioRestClient

class SMSService:

	verified_phone='+YOUR PHONE'
	TWILO_PHONE='+YOUR TWILO PHONE'

	ACCOUNT='YOUR TWILO ACCOUNT'
	TOKEN='YOUR TWILO TOKEN'

	# the following line needs your Twilio Account SID and Auth Token
	client = TwilioRestClient(ACCOUNT, TOKEN)

	# change the "from_" number to your Twilio number and the "to" number
	# to the phone number you signed up for Twilio with, or upgrade your
	# account to send SMS to any phone number

	def send(self, msg):
		self.client.messages.create(to=self.verified_phone, from_=self.TWILO_PHONE, 
       	       	         body=msg)

		print ('message sent: ', msg)
		return

