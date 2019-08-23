import time
import smtplib

#CONFIG. You can change any of the values on the right.
email_provider = 'smtp.gmail.com' #server for your email
email_address = "xxx.com" #your email
email_port = 587 #port for email server
password = "xxx" #your email password
msg = "A neutron walks into a bar and orders a drink. When the neutron gets his drink, he asks, Bartender, how much do I owe you? The bartender replies, For you, neutron, no charge." #your txt message
text_amount = 1 #amount sent
target_email = "xxx@vzwpix.com" #target number. must be in email form- see below for examples
wait = 1 #seconds in between messages
#END CONFIG


# List of servers

# VERIZON @vzwpix.com
# AT&T @mms.att.net

### DO NOT EDIT BELOW THIS LINE ###
server = smtplib.SMTP(email_provider, email_port)
server.starttls()
server.login(email_address, password)
for _ in range(0,text_amount):
    server.sendmail(email_address,target_email,msg)
    print("sent")
    time.sleep(wait)
print("{} texts were sent. Hope you had a good time ;)".format(text_amount))
server.quit()
