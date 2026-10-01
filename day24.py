# #----------------------sending simple message to mail using python-----------------
import smtplib 
from email.message import EmailMessage


sender='**********@gmail.com' #enter the seder mail id
receiver='***********@gmail.com'  #enter the receiver mail id
password='..............'  #enter you app password
message='Hii'
with smtplib.SMTP('smtp.gmail.com',587) as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.sendmail(sender,receiver,message)
print('send')


# --------------------------------------sending to multiple people and with attachments in read mode and body of the mail using python----------------------

sender='**********@gmail.com' #enter the seder mail id
receiver='**********@gmail.com','*****************@gmail.com','************@gmail.com'  #enter the mail of a persons you want to send 
password='......'        #Enter your App password
message=EmailMessage()
message['From']=sender
message['subject']='Python Email project'
message['Bcc']=receiver
message.set_content("hii this email is regarding the project on sending emails through python")
with open('day20.py','rb') as f:
    file=f.read()
message.add_attachment(file,maintype='application',subtype='octet-stream',filename='day20.py')
with smtplib.SMTP('smtp.gmail.com',587) as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.send_message(message)
print('Email send succesfully')