import smtplib #module for sending mails from SMTP

#SMTP object
#Syntax => smtpObj=smtplib.SMTP(host,port,local_hostname)

#Syntax => smtpObj.sendmail(sender, reciever, message)


#Example 1
senderMail='maulikchhabra@gmail.com'
recieverMail='500067458@stu.upes.ac.in'
message= """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(senderMail,recieverMail) 

try:
    password=input('Enter your password: ')
    smtp.Obj=smtplib.SMTP('gmail.com',587)
    smtpObj.login(senderMail,password)
    smtpObj.sendmail(senderMail,recieverMail,message)
    print("Success")
except Exception:
    print("Error: unable to send email")    