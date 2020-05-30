import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "05833dfff32054"
host_pass = "fc875e30b60d71"
guest_address = "sagargarg272@gmail.com"
sender_address = "Enter sender email here"
sender_pass = "Enter sender password here"
recipients_address = "Enter Recipients email here"
subject = " Model Trained "
content = '''Hey, 
				Your model has been trained and desired accuracy is achieved.
			 Your model has been trained and desired accuracy is achieved.
			'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['From'] = sender_address
message['To'] = recipients_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.mailtrap.io', 2525)
session = smtplib.SMTP('Enter your SMTP host', 2525)
session.starttls()
session.login(host_address, host_pass)
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.sendmail(sender_address, recipients_address , text)
session.quit()
print('Mail Sent...')
