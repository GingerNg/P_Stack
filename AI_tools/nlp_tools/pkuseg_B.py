# pkuseg：一个多领域中文分词工具包
# https://github.com/lancopku/pkuseg-python

import pkuseg

seg = pkuseg.pkuseg()           # 以默认配置加载模型
text = seg.cut('我爱北京天安门')  # 进行分词
print(text)