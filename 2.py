import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('rambabuas93@gmail.com','fdhndbhrxjytceel')
subject="birthday party"
body="welcome to learn python"
message="subject:{}\n\n{}".format(subject,body)
listadd=["giridhar05072004@gmail.com","ecekingstar@gmail.com","viya1604@gmail.com"]
print("successfully sent")
ob.quit()
