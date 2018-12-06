#!/usr/bin/python
# -*- coding:utf-8 -*-

# 定义一个类，表示一台远端linux主机
import paramiko
import time
import os
import tarfile

class Linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3

    # 调用该方法连接远程主机
    def connect(self):
        while True:
            # 连接过程中可能会抛出异常，比如网络不通、链接超时
            try:
                self.t = paramiko.Transport(sock=(self.ip, 22))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                # 如果没有抛出异常说明连接成功，直接返回
                print (u'连接%s成功' % self.ip)
                # 接收到的网络数据解码为str
                print (self.chan.recv(65535).decode('utf-8'))
                return
            # 这里不对可能的异常如socket.error, socket.timeout细化，直接一网打尽
            except Exception as e1:
                if self.try_times != 0:
                    print (u'连接%s失败，进行重试' %self.ip)
                    self.try_times -= 1
                else:
                    print (u'重试3次失败，结束程序')
                    exit(1)


    # 断开连接
    def close(self):
        pass

    # 发送要执行的命令
    def send(self, cmd):
        pass

    # get单个文件
    def sftp_get(self, remotefile, localfile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remotefile, localfile)
        t.close()

    # put单个文件
    def sftp_put(self, localfile, remotefile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(localfile, remotefile)
        t.close()

    def get_all_file_in_remote_dir(self,remote_dir):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        # 保存所有文件的列表
        all_files = list()

        # 去掉路径字符串最后的字符'/'，如果有的话
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取当前指定目录下的所有目录及文件，包含属性值
        all_files_attr = sftp.listdir_attr(remote_dir)
        for x in all_files_attr:
            filename = x.filename
            all_files.append(filename)
        t.close()
        return all_files


def work():
    """
    (1)按日期创建文件夹
    （2）sftp connect，get数据
    （3）打包
    （4）将数据包作为邮件附件发送
    crontab 定期执行
    """
    today = time.strftime('%m%d',time.localtime(time.time()))
    today_fold = "PATH"+ today
    today_fold_tar = today_fold+".tar.gz"
    os.makedirs(today_fold)

    host = Linux('XX.XXX.XXX.XXX', 'XXXX', 'XXXX')
    host.connect()
    host.sftp_get("XXXX",today_fold)
    host.close()

    tar = tarfile.open(today_fold_tar, "w:gz")
    tar.add(today_fold)

# 邮件主题 邮件内容 收件人 附件路径'
    send_mail("XXXX数据","","XXXX@XXXX.com",today_fold_tar)


if __name__ == '__main__':
    host = Linux('XX.XXX.XXX.XXX', 'XXX', 'XXXX')
    host.connect()
    file_list = host.get_all_file_in_remote_dir("PATH")
    host.close()
    work()



import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def send_mail(sub,content,mail_to,fileList):
    mail_host='smtp.partner.outlook.cn'
    mail_user='邮箱地址'
    mail_pass='XXXXX'
    mail_to_list=mail_to.split(',')

    msg = MIMEMultipart()
    #msg=MIMEText(content,_charset='utf-8')
    msg['Subject']=sub
    msg['From']=mail_user
    msg['To']=";".join(mail_to_list)
    msg.attach(MIMEText(content,_charset='utf-8'))

    files=fileList.split(',')
    for f in files:
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data
        part.set_payload(open(f, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f).encode('utf-8'))
        msg.attach(part)

    try:
        s=smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(mail_user,mail_to_list,msg.as_string())
        s.close()
        return True
    except Exception as e:
        print (str(e))
        return False



