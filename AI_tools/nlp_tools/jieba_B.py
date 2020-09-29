import jieba
import jieba.analyse
import jieba.posseg as pseg

content = "摄像头可以离开本体， 例如，可以在全球各个地方"
# 词性标注
words = [(word, tag) for word, tag in pseg.cut(content)]
print(words)