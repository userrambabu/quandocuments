import ssl
import smtplib
from email.message import EmailMessage

email_sender="rambabuas93@gmail.com"
email_password="fdhndbhrxjytceel"
email_receiver="ecekingstar@gmail.com"

subject="Hello i am rambabu"
body="""
This is python sample created by rambabu
"""

em=EmailMessage()
em["From"]=email_sender
em["To"]=email_receiver
em["subject"]=subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
    print("Mail sent successfullly")
    
