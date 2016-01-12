#!/usr/local/bin/python3
import time
import random
from twilio.rest import TwilioRestClient


#twilio information - You'll need to update this with your account information.
ACCOUNT_SID = "xxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "yyyyyyyyyyyyyyyyyyyy"
TWILIO_NUMBER = "+18005551212"

#random phrases - you can exted to as many as you would like
phrases = ['hello', 'Awesome', 'Love the pic!', 'snow? really? crazy!', 'OMG so pretty', 'ahhhh.. look at the babies!', 'getting so big', 'you look great']
#phone numbers of the people you would like to bug. Can be any number, remember though you are charged for each message.
phoneNumbers = ['+16615551212', '+16615551213', '+16615551214']

#number of messages you would like to send to each family memeber
numMessages = 10
#min time between messages in seconds
minTime = 60 * 2
#max time between messages in seconds
maxTime = 60 * 10 

def sendMessageTo(toNumber):
	#send message
	global aPhraseIndex
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	client.messages.create(
    to="%s" % toNumber, 
    from_="%s" % TWILIO_NUMBER, 
    body="%s" % phrases[aPhraseIndex]
	)

	time.sleep(3)
	print("Message: %s sent to %s" %(phrases[aPhraseIndex], toNumber))


for i in range(numMessages):
	aPhraseIndex = random.randint(0, len(phrases) -1)

	for singleNumber in (phoneNumbers):
		sendMessageTo(singleNumber)

	
	myTime = random.randint(minTime, maxTime)
	print("I'm going to sleep for %d" % myTime)
	time.sleep(myTime)



