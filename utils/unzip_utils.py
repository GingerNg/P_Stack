#!/usr/bin/python
#coding:utf-8
'''
author:huhaicool@sina.com
date 2015-09-06
version 1.0
python 3.x
'''

import os,os.path
import zipfile

path = "XXX"


# password='1234'

def pojie_zip(path, password):
    if path[-4:] == '.zip':
        # path = dir+ '\\' +file
        # print path
        zip = zipfile.ZipFile(path, "r", zipfile.zlib.DEFLATED)
        # print zip.namelist()
        try:
            # 若解压成功，则返回True,和密码
            zip.extractall(path='C:\\Users\\Administrator\\Desktop\\', members=zip.namelist(), pwd=password)
            print (' ----success!,The password is %s' % password)
            zip.close()
            return True
        except:
            pass  # 如果发生异常，不报错
        print ('error')


def get_pass():
    # 密码字典的路径
    passPath = 'C:\\Users\\Administrator\\Desktop\\zip.txt'
    passFile = open(passPath, 'r')
    for line in passFile.readlines():
        password = line.strip('\n')
        print ('Try the password %s' % password)
        if pojie_zip(path, password):
            break
    passFile.close()






def translateDir(path):
    for fname in path:
        try:
            newName = fname.encode("cp437").decode("utf-8",'ignore')
            print(newName)
            # os.rename(os.path.join(root, fname), os.path.join(root, newName))
        except Exception as e:
            print(e)



    # for root, dirs, files in os.walk(path):
    #     for dname in dirs:
    #         try:
    #             # dname = dname.decode('cp437')
    #             newName = dname.encode("cp437").decode("gbk",'ignore')
    #             os.rename(os.path.join(root, dname), os.path.join(root, newName))
    #         except Exception as e:
    #             print(e)
    #             # pass
    #
    #     for fname in files:
    #         try:
    #             newName = fname.encode("cp437").decode("gbk",'ignore')
    #             os.rename(os.path.join(root, fname), os.path.join(root, newName))
    #         except Exception as e:
    #             print(e)

# def unzip(Afile,filepath): #传入文件名和路径，解压到单独的文件夹,并删除文件名中指定关键字
#     import os
#     import zipfile
#     myzip=zipfile.ZipFile(filepath+Afile,'r')
#     myfilelist=myzip.namelist()
#     for name in myfilelist:
#         strname = name.encode('cp437').decode('gbk')
#         if strname == "readme.html"or strname =="": #判断文件名，如果文件名是不需要的就不解压
#             pass
#         else:
#             strname=strname.replace('_lanrentuku.com','')
#             path = filepath+Afile.split(".")[0]+"\\"
#             dirpath(path)
#             f_handle=open(path+strname,"wb")
#             f_handle.write(myzip.read(name))
#             f_handle.close()
#     myzip.close()


def fir_unzip():
    zp = zipfile.ZipFile("./111.zip")
    nlist = zp.namelist()

    # os.mkdir("./测试zip解压缩")

    for n in nlist:

        try:
            m = "./" + n.encode("cp437").decode("utf8")
        except:
            m = "./" + n.encode("cp437").decode("gbk")

        print(m)
        if m.endswith('/'):
            continue

        if not os.path.exists(os.path.dirname(m)):
            os.makedirs(os.path.dirname(m))

        open(m, 'wb').write(zp.read(n))

    zp.close()


if __name__ == '__main__':
    #zip_dir(r'/tmp/xungou',r'/tmp/xungou.zip')
    # unzip_file(r'111.zip',r'./')
    name = "111"
    f_path = name + ".zip"
    zp = zipfile.ZipFile(f_path, "r")

    fir_unzip(zp)
    # d_path = name
    # names = zp.namelist()
    #
    # zip_list = zp.namelist()
    # for zipfile in zip_list:
    #     # print(zipfile)
    #     # print(zipfile.encode('utf-8'))
    #     try:
    #         zipfile = zipfile.encode('cp437').decode('gbk')
    #     except:
    #         zipfile = zipfile.encode('utf-8').decode('utf-8')


    # zp.extractall(d_path)
    # translateDir(d_path)
    # zp.close()

    i = 4
    while file_util.isexisted('/home/XX/task/2/2/'+str(i)+'.zip'):
        zip = zipfile.ZipFile('/home/XX/task/2/2/'+str(i)+'.zip', "r", zipfile.zlib.DEFLATED)
        passwd = file_util.read_file_by_line('/home/XX/task/2/2/'+str(i)+'.txt')
        zip.extractall(path='/home/XX/task/2/2', members=zip.namelist(), pwd=passwd)
        i +=1