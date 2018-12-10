# using_temple
# BatchRename
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
for i, filename in enumerate(photofiles):  # i : 0,1,2...
    base, ext = os.path.splitext(filename)  # wordsegmentation
    print(base, ext)
    newname = t.substitute(d=date, n=i, f=ext)
    print(i)
    print('{0} --> {1}').format(filename, newname)
