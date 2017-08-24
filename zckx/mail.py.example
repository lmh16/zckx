import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
 
 
def send_mail(): 

    sender = 'li.mu.han@hotmail.com'
    receivers = ['junxunpostie@hotmail.com']  
    
    msgRoot = MIMEMultipart('related')
    title = open('title.txt')
    subject = title.read()
    title.close()
    msgRoot['Subject'] = Header(subject.decode('utf-8'))
     
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
     
    msg = open('content.txt')
    mail_msg = msg.read()
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # read all images
    x = 1
    for root, dirs, files in os.walk('./'):
        for name in files:
            if name == 'content.txt' or name == 'title.txt':
                continue

            fp = open(name, 'rb')
            msgImage = MIMEImage(fp.read(), _subtype=name.split('.')[1])
            fp.close()
            msgImage.add_header('Content-ID', 'image%i'%x)
            msgRoot.attach(msgImage)
            x += 1
                
        break # walk once under ./
     
    try:
        s = smtplib.SMTP() 
        s.connect('smtp-mail.outlook.com', 587) 
        s.ehlo()
        s.starttls()
        s.ehlo()    
        #s.login('login_name','password')  
        s.sendmail(sender, receivers, msgRoot.as_string())
    except smtplib.SMTPException, e:
        print repr(e)
