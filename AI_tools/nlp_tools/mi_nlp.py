from minlptokenizer.tokenizer import MiNLPTokenizer

# https://github.com/XiaoMi/MiNLP
# TODO

tokenizer = MiNLPTokenizer(granularity='fine')  # fine：细粒度，coarse：粗粒度，默认为细粒度
print(tokenizer.cut('今天天气怎么样？'))