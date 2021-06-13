import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#EMAIL_ADDRESS = 'cisco.kidicantec@googlemail.com'
#EMAIL_PASSWORD = 'Coreldraw1$'


#contacts = ['cisco.kidicantec@googlemail.com', 'mariowakeham@outlook.com']
#contacts = ['mario@wakeham.name','mariowakeham@outlook.com','cisco.kidicantec@googlemail.com']
contacts = ['mariowakeham@outlook.com','cisco.kidicantec@googlemail.com']


msg = EmailMessage()
msg['Subject'] = 'This email is from python Sunday 13th June 2021 20:51!'
msg['From'] = EMAIL_ADDRESS
#msg['To'] = 'mario@wakeham.name'
#msg['To'] = 'mariowakeham@outlook.com'
#msg['To'] = contacts
msg['To'] = ', '.join(contacts)
#msg['To'] = "mariowakeham@outlook.com","mariowakeham@outlook.com","cisco.kidicantec@googlemail.com"
msg.set_content('Image Attached and html')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style='color:SlateGray;'>This is an HTML Email from python! 20:14</h1>
    </body>
</html>
""", subtype='html')


#files = ['C:/pythonestates/static/uploadimages/IMG_20190429_181624_2.jpg', 'C:/pythonestates/static/uploadimages/helen.jpg','C:/pythonestates/static/uploadimages/estate.css','C:/Compress/LibreCAD_Users_Manual_2.1.3.pdf']
files = ['C:/Compress/1984-86s600deck.pdf']



for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        #file_type = imghdr.what(f.name)
        file_name = f.name
        #print(file_type)
    #msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
