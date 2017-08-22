#-*- coding:utf-8 -*-
import mail
import os

walkroot="D:/zckx/zckx/posts"
for root, dirs, files in os.walk(walkroot):
    if root!=walkroot:
        break
    for name in dirs:
        if name == "mail":
            continue
        
        os.chdir(os.path.join(walkroot, name))
        mail.send_mail()
        os.chdir("..")