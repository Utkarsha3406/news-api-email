import smtplib
import ssl
import os

def send_email(message):
    host="smtp.gmail.com"
    port=465

    username="up3406@srmist.edu.in"
    password=os.getenv("PASSWORD")
#environment variable used to store value of actual password
#to get environment variable search in the start menu of computer

    receiver="up3406@srmist.edu.in"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)