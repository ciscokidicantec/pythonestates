import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#EMAIL_ADDRESS = 'cisco.kidicantec@googlemail.com'
#EMAIL_PASSWORD = 'Coreldraw1$'


contacts = ['cisco.kidicantec@googlemail.com', 'mariowakeham@outlook.com']

msg = EmailMessage()
msg['Subject'] = 'This email is from python 21:04!'
msg['From'] = EMAIL_ADDRESS
#msg['To'] = 'mario@wakeham.name'
msg['To'] = 'mariowakeham@outlook.com'


msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email from python!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
