##https://www.youtube.com/watch?v=g_j6ILT-X0k
##myaccount.google.com\

import smtplib
from email.message import EmailMessage
import os
import imghdr

sender_mail_id = 'zcoer.it.seb116@gmail.com'
password = 'fhiywumcufkiekqe'

def send(subject,send_to,message):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_mail_id
    msg['To'] = send_to

    msg1 = "Thank you for submitting your feedback\n\nYour feedback message is: \n\t\t"
    
    msg.set_content(msg1 + message)

    with open('image5.jpg','rb') as m:

        file_data = m.read()
        file_type = imghdr.what(m.name)
        file_name = m.name

    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename=subject + '.png')

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sender_mail_id,password)
        smtp.send_message(msg)

# send('Feedback Message acknowledgement', 'ajayladkat123@gmail.com','Hello. Nice Application ')

