from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
import requests
import sys
if __name__ == '__main__':
    # content = "说到飞机呀，人们第一就会想到莱特兄弟"
    content = "老师为你们的优秀，点赞。"
    # content = "第一行，谁来领读？"
    # content = "我们一起来看看，好不好"
    form_data = {
        "sentence": content
    }
    resp = requests.post("http://192.168.235.231:8000/textmatchpose", data=form_data)
    if resp.status_code == 200:
        print(resp.json())
        pose_pth = resp.json()["result"]
        pth = pose_pth.split("/")[-2]
        app = QApplication(sys.argv)
        player = QMediaPlayer()
        vw = QVideoWidget()                       # 定义视频显示的widget
        vw.show()
        player.setVideoOutput(vw)                 # 视频播放输出的widget，就是上面定义的
        # file_path = QFileDialog.getOpenFileUrl()[0]
        # pth = "向前说话03_男老师_陈述_告诉你们_7bf4d822-42cf-4a43-af0d-6534067ae117"
        file_path = QUrl("file:///home/ginger/Videos-20200208/{}.mp4".format(pth))
        # print(file_path)
        player.setMedia(QMediaContent(file_path))  # 选取视频文件
        player.play()                               # 播放视频
        # sys.exit()
        sys.exit(app.exec_())
