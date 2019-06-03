import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail_sending(first_name,emailid,link):

        msg= MIMEMultipart()

        msg["From"] ="user registration"
        msg["To"]=emailid
        msg["Subject"]="Verification Link"

        body="Hello " +first_name+ " \n Please click on the link below to activate the user account and login =  " +link
        msg.attach(MIMEText(body,"plain"))

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("ramannetmax@gmail.com","8053948969")
        text=msg.as_string()
        server.sendmail("ramandhiman1322@gmail.com",
                    emailid,text)

        server.quit()
        print("message sent to "+ first_name +" successfully")


