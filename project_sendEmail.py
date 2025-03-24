import smtplib #  python library for sending emails
from email.mime.text import MIMEText # represent the email content as plain text

body= 'This is a python code to send emails'
subject= 'test send'
sender= "sender's_email_address"
recipient= ['1stPersonEmail','2ndPersonEmail']
password= "sender's_email_password"

def send_email(body,subject,sender,recipient,password):
    msg= MIMEText(body) # msg = now msg is the new MIME object containing the email body text
    msg['Subject']= subject # msg is now set with the subject, sender, and recipients.
    msg['From']= sender
    msg['To']= ', '.join(recipient) # joining the multiple recipients with ', '  
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: # create a secure connection to Gmail SMTP  
        server.login(sender, password)                      # server on port 465
        server.sendmail(sender, recipient, msg.as_string())  

    print("Message sent")

send_email(body,subject,sender,recipient,password)