from keras.preprocessing.text import Tokenizer
import keras
from collections import OrderedDict
import jieba
from typing import List
# jieba.add_word("不可抗力",99,"nz")
# https://github.com/fxsjy/jieba


def segment(content):
    """
    单line分词
    """
    if "：" in content:
        result = (str(content.split("：")[1])).replace(
            "\r\n", "").strip()  # 删除多余空行与空格
    else:
        result = content
    cutResult = jieba.lcut(result)  # 默认方式分词，分词结果用空格隔开
    return " ".join(cutResult)


def batch_segment(lines):
    """
    批量lines分词
    """
    seg_lines = []
    for line in lines:
        seg_lines.append(segment(line))
    return seg_lines


tokenizer = keras.preprocessing.text.Tokenizer(num_words=None,
                                               filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n',
                                               lower=True,
                                               split=" ",
                                               char_level=False)


def corpus2vocab_keras(lines) -> Tokenizer:
    """
    lines: list,sentences
    keras 词频统计
    """
    seg_lines = batch_segment(lines)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(seg_lines)
    # `0` is a reserved index that won't be assigned to any word.
    return tokenizer


def sent2seq(sent, tokenizer) -> List:
    """
    func:句子生成word_index序列
    sent: sentence,str
    """
    texts = [segment(sent)]
    # tokenizer = Tokenizer()
    return keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences(texts),
                                                      maxlen=100,
                                                      padding="post",
                                                      truncating="post")[0]


text = ["今天北京下雨了", "我今 加班"]
print(corpus2vocab_keras(text).word_counts)

text = ["我们乙方根据甲方的委托承包甲方指定的生产线项目"]
tokenizer = corpus2vocab_keras(text)
print(sent2seq("我们乙方根据甲方的委托承包甲方指定的生产线项目，并与甲方共同选派作业人员，在遵守甲方的有关",
               tokenizer))
