from http import server
import os
import smtplib,ssl
import imghdr

from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import mysql.connector

#import win32com.client

#from datetime import datetime, timedelta

mydbestate = mysql.connector.connect(host='localhost',user='root',passwd='Coreldraw1$')
mycursorestate = mydbestate.cursor()
sql = 'DROP DATABASE IF EXISTS ESTATE'
mycursorestate.execute(sql)
mycursorestate.execute('CREATE DATABASE ESTATE')
mycursorestate.close()
mydbestate.close()

mydbestate = mysql.connector.connect(host='localhost',user='root',passwd='Coreldraw1$',database='ESTATE')
mydbestatecursor = mydbestate.cursor()
mydbestatecursor.execute('CREATE TABLE ESTATES (estatename VARCHAR(50))')
mydbestatecursor.close()
mydbestate.close()
mydb = mysql.connector.connect(host='localhost',user='root',passwd='Coreldraw1$',database='world')
mycursor = mydb.cursor()
mycursor.execute('select * from city')
result = mycursor.fetchall()
mycursor.close()
mydbestate.close()

for i in result:
    print(i)

msg = MIMEMultipart()
mysubject = 'Sending Email From Python'

emailserver = smtplib.SMTP('smtp.gmail.com',587)
emailserver.starttls()
emailserver.login('cisco.kidicantec@googlemail.com','Coreldraw1$')

message = 'sending this message from python'
emailserver.sendmail('cisco.kidicantec@googlemail.com','mario@wakeham.name',message)
emailserver.quit()


#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#EMAIL_ADDRESS = 'cisco.kidicantec@googlemail.com'
#EMAIL_PASSWORD = 'Coreldraw1$'

EMAIL_ADDRESS = 'mariowakeham@mario.wakeham.name'
EMAIL_PASSWORD = 'Coreldraw1$1'

msg = EmailMessage()
msg['Subject'] = 'This email is from python 21:04!'
msg['From'] = 'cisco.kidicantec@googlemail.com'
msg['To'] = 'mario@wakeham.name'
#msg['To'] = 'mariowakeham@outlook.com'
msg.set_content('This is the body of an email message from python 7th May 2022 23:45')

files = ['hondacabledoglegend.jpg','helen_hair.jpg','hondacableloopend.jpg','helen_hair_rotated.jpg']

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data,maintype='image',subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login('cisco.kidicantec@googlemail.com', 'Coreldraw1$')
    smtp.send_message(msg)


#with smtplib.SMTP_SSL('smtp-mail.outlook.com',465) as smtp:
#   smtp.login('mariowakeham@outlook.com', 'Coreldraw2$')
#    smtp.send_message(msg)

contacts = ['cisco.kidicantec@googlemail.com', 'mariowakeham@outlook.com']

"""outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'mario@wakeham.name'
mail.Subject = 'Sample Email'
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = "This is the normal body"
#mail.Attachments.Add('c:\\sample.xlsx')
#mail.Attachments.Add('c:\\sample2.xlsx')
#mail.CC = 'somebody@company.com'

mail.Send()
"""
"""
msg = EmailMessage()
msg['Subject'] = 'This email is from python 21:04!'
msg['From'] = EMAIL_ADDRESS
#msg['To'] = 'mario@wakeham.name'
msg['To'] = 'mariowakeham@outlook.com'


#msg.set_content('This is a plain text email')

#msg.add_alternative("""\
#<!DOCTYPE html>
#<html>
#    <body>
 #       <h1 style="color:SlateGray;">This is an HTML Email from python!</h1>
  #  </body>
#</html>
""", subtype='html')

context = ssl.create_default_context

#with smtplib.SMTP_SSL('localhost') as smtp:
 #   smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
  #  smtp.send_message(msg)


  

with smtplib.SMTP_SSL('mail.mario.wakeham.name',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
"""
