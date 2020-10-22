import jieba
import jieba.analyse
import jieba.posseg as pseg

content = "摄像头可以离开本体， 例如，可以在全球各个地方"
# 词性标注
words = [(word, tag) for word, tag in pseg.cut(content)]
print(words)


# jieba.load_userdict("C:/Users/idmin/Desktop/dict.txt")
content = "八一男篮，即八一南昌红谷滩男篮，2018-2019赛季之前称八一双鹿电池男篮，是CBA老牌劲旅，自建队以来，发扬解放军优良传统和作风，本着为国争光，为军队争光的高度荣誉感和使命感，严格治队，严格训练，形成勇猛顽强，敢打敢拼，团结协作的战斗作风和注重防守、快速、准确、内外结合的技战术风格。"
# 词性标注
words = [(word, tag) for word, tag in pseg.cut(content)]
print(words)

jieba.add_word("八一双鹿电池男篮", tag="nz-sport", freq="1000")
words = [(word, tag) for word, tag in pseg.cut(content)]
print(words)
