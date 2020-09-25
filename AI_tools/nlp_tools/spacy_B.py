import spacy
# 下载模型：
# python3 -m spacy download en_core_web_sm

# 中文模型：https://github.com/howl-anderson/Chinese_models_for_SpaCy

# 安装： pip3 install zh_core_web_sm-2.x.x.tar.gz

# spacy link zh_core_web_sm zh： 使用 zh 这个别名来访问这个模型

# 安装：pip3 install spacy
# https://github.com/explosion/spacy-models/releases//tag/zh_core_web_sm-2.3.1
"""
pos 词性标注
dep 依存分析
"""
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"This is a sentence.")
print([(w.text, w.pos_, w.dep_) for w in doc])

txt = ''''European authorities fined Google a record $5.1 billion
on Wednesday for abusing its power in the mobile phone market and
ordered the company to alter its practices'
'''
doc = nlp(txt)
ners = [(ent.text, ent.label_) for ent in doc.ents]
print(ners)

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"This is a sentence.")
print([(w.text, w.pos_) for w in doc])