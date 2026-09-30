#----------------------sending simple message to mail using python-----------------
import smtplib 
from email.message import EmailMessage
sender='naralaanushareddy2@gmail.com'
receiver='naralaanushareddy52@gmail.com'
password='finmfyvdtyineutr'
message='Hii'
with smtplib.SMTP('smtp.gmail.com',587) as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.sendmail(sender,receiver,message)
print('send')


# --------------------------------------sending to multiple people and with attachments in read mode and body of the mail using python----------------------

sender='naralaanushareddy2@gmail.com'
receiver='naralaanushareddy52@gmail.com','navyasreelankapothu@gmail.com','furusage@gmail.com'
password='finmfyvdtyineutr'
message=EmailMessage()
message['From']=sender
message['To']=receiver
message['subject']='Python Email project'
message['Bcc']='receiver'
message.set_content("hii this email is regarding the project on sending emails through python")
with open('day20.py','rb') as f:
    file=f.read()
message.add_attachment(file,maintype='application',subtype='octet-stream',filename='day20.py')


with smtplib.SMTP('smtp.gmail.com',587) as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.send_message(message)
print('Email send succesfully')