import os
import shutil
import sys
"""
文件处理工具集合
"""

def batch_mv(fold_path1,fold_path2,new_fold_path):
    """
    将fold2中不在fold1的文件移动到new_fold
    :param fold_path1:
    :param fold_path2:
    :param new_fold_path:
    :return:
    """
    fold1 = os.listdir(fold_path1)
    for dirpath, dirnames, filenames in os.walk(fold_path2):
        for filename in filenames:
            if filename not in fold1:
                shutil.copy(os.path.join(fold_path2,filename), os.path.join(new_fold_path,filename))

def lookfor_files(fold_path1,fold_path2):
    """
    找出fold2中不在fold1中的文件名
    :param fold_path1:
    :param fold_path2:
    :return:
    """
    fold1 = os.listdir(fold_path1)
    for dirpath, dirnames, filenames in os.walk(fold_path2):
        for filename in filenames:
            if filename+".csv" not in fold1:
                print(filename)

def batch_rename(fold_path):
    from string import Template
    import time, os.path

    photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

    class BatchRename(Template):  # subclass  of temple
        delimiter = '%'

    # fmt = input('Enter rename style(%d-date %n-seqnum %f-format): ')
    fmt = 'Ashley_%n%f'

    t = BatchRename(fmt)  # create a object
    print(t)
    date = time.strftime('%d%d%y')  # return a string as time
    print(date)
    for i, filename in enumerate(photofiles):  # i : 0,1,2...   (index value)
        base, ext = os.path.splitext(filename)  # wordsegmentation
        print(base, ext)
        newname = t.substitute(d=date, n=i, f=ext)
        print(i)
        print('{0} --> {1}').format(filename, newname)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise ValueError("""usage: python tools.py methods fold1 fold2 fold3""")
    if sys.argv[1] == "mv":
        batch_mv(sys.argv[2],sys.argv[3],sys.argv[4])
    elif sys.argv[1] == "lookfor":
        lookfor_files(sys.argv[2],sys.argv[3])