#!/usr/bin/python
# coding:utf8

# from basic.meta_class import APIBase    # from module import class
from basic.meta_class.API.APIBase import APIBase


class ImAGoodBoy(APIBase):
    a_polite_attribute = 1

# [Output] Well done! You are a polite coder!

class FuckMyBoss(APIBase):
    pass

# [Output] NameError: Sensitive words "fuck" detected in the string "FuckMyBoss".

class PretendToBePolite(APIBase):

    def __fuck_your_asshole(self):
        pass

# [Output] NameError: Sensitive words "asshole", "fuck" detected in the string "_PretendToBePolite__fuck_your_asshole".

if __name__=='__main__':
    pretendToBePolite = PretendToBePolite()
    imAGoodBoy = ImAGoodBoy()
