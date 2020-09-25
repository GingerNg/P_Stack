# -*- cobert_encg:utf-8 -*-
from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity
# https://github.com/hanxiao/bert-as-service
# 启动server端：bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=4


class Encoding(object):
    def __init__(self):
        self.server_ip = "127.0.0.1"
        self.bert_client = BertClient(ip=self.server_ip, check_length=False)

    def encode(self, query):
        tensor = self.bert_client.encode([query])
        return tensor

    def encodes(self, queries):
        tensors = self.bert_client.encode(queries)
        return tensors

    def query_similarity(self, query_list):
        tensors = self.bert_client.encode(query_list)
        return cosine_similarity(tensors)[0][1]


ec = Encoding()


def bert_enc(sents):
    def isempty(sent):
        if not sent or sent.strip() == "":
            return "其它"
        else:
            return sent
    sents = list(map(isempty, sents))
    return ec.encodes(sents)
