import PySimpleGUI as sg

# -*- coding: utf-8 -*-# @Time : 2019/1/18 9:46# @Author : wujf# @Email : 1028540310@qq.com# @File : tkinter_02.py# @Software: SublimTextsg.ChangeLookAndFeel('GreenTan')
form = sg.FlexForm('PySimpleGUI入门软件', default_element_size=(40, 1))
column1 = [[sg.Text('个人评估', background_color='#d3dfda', justification='center', size=(10,1))],
           [sg.Spin(values=('1','2', '3','4','5','6', '7','8', '9','10'), initial_value='工作能力')],
           [sg.Spin(values=('1','2', '3','4','5','6', '7','8', '9','10'), initial_value='同事相处')],
           [sg.Spin(values=('1','2', '3','4','5','6', '7','8', '9','10'), initial_value='团队协作')]]
layout = [
    [sg.Text('个人简历', size=(30, 1), font=("Helvetica", 25)),sg.Text('Writer：Mr wu', size=(60, 1),font=("Helvetica",10))],
    [sg.Text('自我介绍', size=(60, 1),font=("Helvetica", 10))],
    [sg.InputText('执着于技术的探索，代码就是一切！')],
    [sg.Text('个人爱好')],
    [sg.Checkbox('游泳'),
        sg.Checkbox('看书'),
        sg.Checkbox('打羽毛球', default=True),
        sg.Checkbox('打保龄球'),
        sg.Checkbox('打兵球'),
        sg.Checkbox('打篮球'),
        sg.Checkbox('打棒球'),
        sg.Checkbox('唱歌'),
        sg.Checkbox('跳舞'),
        sg.Checkbox('玩游戏'),
        sg.Checkbox('旅游')
    ],
    [sg.Text('性别')],
    [sg.Radio('男     ', "RADIO1", default=True), sg.Radio('女', "RADIO1")],
    [sg.Text('出生')],
    [sg.Listbox(values=('1990年','1991年','1992年','1993年','1994年','1995年','1996年','1997年','1998年','1999年','2000年','2001年','2002年','2003年'), size=(30, 5))],
    [sg.Text('工作简介')],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(50, 5))],
    [sg.Text('工作经历')],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(70, 8))],
    [sg.Text('语言')],
    [sg.InputCombo(('汉语', '英语','德语', '法语','韩语', '意大利语','俄语', '日语','其他'), size=(20, 6)),
     sg.Text('语言能力'),
     sg.Slider(range=(1, 100), orientation='h', size=(20, 20), default_value=65)],
     [sg.InputCombo(('汉语', '英语','德语', '法语','韩语', '意大利语','俄语', '日语','其他'), size=(20, 6)),
     sg.Text('语言能力'),
     sg.Slider(range=(1, 100), orientation='h', size=(20, 20), default_value=65)],
    [sg.Text('你的学历')],
    [sg.Listbox(values=('高中','大专', '本科','硕士', '博士','海外引进人才'), size=(30, 5)),
     sg.Text('行业认知度'),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
     sg.Text('工作热情度'),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
     sg.Text('效率执行度'),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
     sg.Column(column1, background_color='#d3dfda')],
    [sg.Text('_'  * 80)],
    [sg.Text('上传附件简历', size=(35, 1))],
    [sg.Text('目录', size=(15, 1), auto_size_text=False, justification='right'),
     sg.InputText('默认目录'), sg.FolderBrowse('浏览')],
    [sg.Submit('确认'), sg.Cancel('取消')]
     ]
button, values = form.Layout(layout).Read()
sg.Popup(button,values)  #（python3.0以上不再写成 sg.Msgbox()）