# -*- coding: utf-8 -*-
from pyltp import SementicRoleLabeller
from pyltp import Segmentor
from pyltp import Parser, Postagger
import os
#######################
# https://pyltp.readthedocs.io/zh_CN/develop/api.html#id21

# 命名实体识别 'ner.model'

# 语义角色标注 模型目录为`srl`
#######################################
# 分词：模型名称为`cws.model`
LTP_DATA_DIR = '/home/ginger/Projects/StaticResource/ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，

segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
words = segmentor.segment('元芳你怎么看')  # 分词
print(' '.join(words))
segmentor.release()  # 释放模型
#########################################
# 词性标注 `pos.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
postagger = Postagger()  # 初始化实例
postagger.load(pos_model_path)  # 加载模型

words = ['摄像头', '可以', '离开', '本体']  # 分词结果
postags = postagger.postag(words)  # 词性标注

print('\t'.join(postags))
postagger.release()  # 释放模型

#########################################
# 依存句法分析 'parser.model'　
parser = Parser()  # 初始化实例
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')
parser.load(par_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
arcs = parser.parse(words, postags)  # 句法分析

print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
parser.release()  # 释放模型

########################################
srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl.model')

labeller = SementicRoleLabeller()  # 初始化实例
labeller.load(srl_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
# arcs 使用依存句法分析的结果
roles = labeller.label(words, postags, arcs)  # 语义角色标注

# 打印结果
for role in roles:
    print(role.index, "".join(["%s:(%d,%d)" % (
        arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
labeller.release()  # 释放模型
