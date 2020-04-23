# -*- coding: utf-8 -*-
# ht_script.py
# @author Ginger
# @description
# @created 2020-03-09T18:49:24.501Z+08:00
#


import os
import zipfile
import re


def zip_dir(file_path, zfile_path):
    '''
    function:压缩
    params:
        file_path:要压缩的件路径,可以是文件夹
        zfile_path:解压缩路径
    description:可以在python2执行
    '''
    filelist = []
    if os.path.isfile(file_path):
        filelist.append(file_path)
    else:
        for root, dirs, files in os.walk(file_path):
            for name in files:
                filelist.append(os.path.join(root, name))
                print('joined:', os.path.join(root, name), dirs)

    zf = zipfile.ZipFile(zfile_path, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(file_path):]
        print(arcname, tar)
        zf.write(tar, arcname)
    zf.close()


def unzip_file(zfile_path, unzip_dir):
    '''
    function:解压
    params:
        zfile_path:压缩文件路径
        unzip_dir:解压缩路径
    description:
    '''
    try:
        with zipfile.ZipFile(zfile_path) as zfile:
            zfile.extractall(path=unzip_dir)
    except zipfile.BadZipFile as e:
        print(zfile_path+" is a bad zip file ,please check!")


def ht(src_file_name, dest_file_name, res_file_name, work_path):
    src_file_path = work_path + src_file_name + ".docx"
    src_dir = work_path + src_file_name
    unzip_file(zfile_path=src_file_path, unzip_dir=src_dir)
    src_xml_doc = open(os.path.join(src_dir, "word", "document.xml")).read()

    # <m:oMathPara>  </m:oMathPara>
    a = [m.end() for m in re.finditer("<w:body>", src_xml_doc)]
    e = [m.start() for m in re.finditer("</w:body>", src_xml_doc)]
    content = src_xml_doc[a[0]+1:e[0]]
    open("./contentt.xml", "w").write(content)

    dest_file_path = work_path + dest_file_name + ".docx"
    dest_dir = work_path + dest_file_name
    unzip_file(zfile_path=dest_file_path, unzip_dir=dest_dir)

    dest_xml_doc = open(os.path.join(dest_dir, "word", "document.xml")).read()

    a = [m.end() for m in re.finditer(
        "<w:bookmarkStart", dest_xml_doc)]
    start = a[0]
    while dest_xml_doc[start] != ">":
        start += 1
    e = [m.start() for m in re.finditer("<w:bookmarkEnd", dest_xml_doc)]
    print(a, e)
    res_xml = dest_xml_doc[0:start+1]+content+dest_xml_doc[e[0]:]
    open(os.path.join(dest_dir, "word", "document.xml"), "w").write(res_xml)
    zip_dir(file_path=dest_dir, zfile_path=work_path+res_file_name)


if __name__ == "__main__":
    """[将src_file插入dest_file,生成res_file]
    """
    work_path = os.getcwd() + "/file_tools/word_tool/海通产品中心需求/"
    ht(src_file_name="1、插入数据", dest_file_name="2、产品中心产生文档",
       res_file_name="result.docx")
