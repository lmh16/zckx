'''import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
 
sender = 'li.mu.han@hotmail.com'
receivers = ['junxunpostie@hotmail.com']  
 
msgRoot = MIMEMultipart('related')
subject = 'Python SMTP'
msgRoot['Subject'] = Header(subject)
 
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
 
 
msg = open('content.txt')
mail_msg = msg.read()
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

fp = open('1.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
 
# define picture id and use it in message
msgImage.add_header('Content-ID', 'image1')
msgRoot.attach(msgImage)
 
try:
    s = smtplib.SMTP() 
    s.connect('smtp-mail.outlook.com', 587) 
    s.ehlo()
    s.starttls()
    s.ehlo()    
    #s.login('','')  
    s.sendmail(sender, receivers, msgRoot.as_string())
except smtplib.SMTPException, e:
    print repr(e)'''

def send_mail():
    print "sth."
    pass