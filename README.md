# GroupMessage
I hate group messages. So I wrote a quick Twilio powered app to torture my family.

##Get a twilio account [here](https://www.twilio.com)
https://www.twilio.com/

You'll need to charge up some time. I put up $20 and that was more than enough to play with until I was bored. 

##Required Stuffs
sudo apt-get install python3  
sudo apt-get install python3-pip  
sudo pip3 install twilio

  
  

**Information that you get from your twilio account**

```
#twilio information - You'll need to update this with your account information.
ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
TWILIO_NUMBER = "+16615551212"
```
**other configuration**

```
#random phrases - you can exted to as many as you would like
phrases = ['hello', 'Awesome', 'Love the pic!', 'snow? really? crazy!', 'OMG so pretty', 'ahhhh.. look at the babies!', 'getting so big', 'you look great']
#phone numbers of the people you would like to bug. Can be any number, remember though you are charged for each message.
phoneNumbers = ['+18055551212', '+17755551212', '+11235551212']

#number of messages you would like to send to each family member
numMessages = 10
#min time between messages in seconds
minTime = 60 * 2
#max time between messages in seconds
maxTime = 60 * 10 
```

**phrases** - phrases that you would like to send  
**phoneNumbers** - phone numbers of people you would like to bug  
**numMessages** - number of messages that you would like to send to each family member.  
**minTime** - minimum time in seconds between messages. Note that there will be 3 seconds between messages because of limit set by twilio. and the * 60 thing is so that you can figure out minutes... see what I did there?  
**maxTime** - same as above but like different.  

**note** - Use as you wish. No warrenty or responsibility for anything. I just thought this was funny more so than anything. Try not to make anyone too angry.

I can't spell... and I don't care.  

Have fun!  
Cody

