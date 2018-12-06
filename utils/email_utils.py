# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
# from email.MIMEMultipart import MIMEMultipart
from email.header import Header
import datetime
import time
import os
import sys


class Email (object ):
    def __init__ (self,domain,port,account,password,display=None):
        """ 
        Gmail("username@gmail.com","xxxx") 
        """ 
        self.domain = domain
        self.port = port
        self.account = account
        self.password = password
        self.display = display or self.account

    def send (self,to,title,content,_t=str(datetime.datetime.now())):
        """ 
        send('username@gmail.com,other@domain.com") 
        """ 
        try:
            server = smtplib.SMTP(self.domain, self.port)
        except smtplib.SMTPConnectError:
            return 0, u"无法连接邮件服务器".encode("utf-8")
        #server.set_debuglevel(1)
        server.docmd("EHLO server" )
        server.starttls()
        try:
            server.login(self.account,self.password)
        except smtplib.SMTPAuthenticationError:
            return 0, u"用户名或者密码错误".encode("utf-8")
        #邮件主体
        h = Header(title, 'utf-8')
        
        
        #创建一个带附件的实例
        #msg = MIMEMultipart()
        msg = MIMEText(content,'html','utf-8')
        
        #构造附件
        #att = MIMEText(open(fn, 'rb').read(), 'base64', 'utf-8')
        #att["Content-Type"] = 'application/octet-stream'
        #att["Content-Disposition"] = 'attachment; filename="%s"'%os.path.basename(fn)
        #msg.attach(att)
        
        msg['Subject' ] = h
        msg['From' ] = self.display
        msg['To' ] = to
        msg['Date' ] = time.strftime('%a, %d %b %Y %H:%M:%S %z') 
        
        try:
            server.sendmail(self.account, to.split(',') ,msg.as_string())
        except smtplib.SMTPRecipientsRefused:
            return 0, u"邮件发送失败".encode("utf-8")
        server.close()
        return 1, u"发送成功"
        
        
        
EMAIN_DOMAIN = 'smtp.partner.outlook.cn'
SERVER_PORT = 587
EMAIL_USER_NAME = "XXX@XXX.com"
EMAIL_PASSWORD = "********"

def send(to_list,title, content):
    mail = Email(EMAIN_DOMAIN,SERVER_PORT,EMAIL_USER_NAME,EMAIL_PASSWORD,
                               'XXXX@XXXX.com')
    return mail.send(",".join(to_list), title, content)
    
    

if __name__ == "__main__":
    print (send(["XXX@XXX.com","xxx@XXX.com"], "XXXX，XXXX", "XXXX"))
