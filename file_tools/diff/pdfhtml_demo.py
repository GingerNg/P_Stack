from bs4 import BeautifulSoup
import re

import difflib
"""
https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27
"""


class DocxDiff(difflib.HtmlDiff):
    def __init__(self):
        super().__init__()

    #         self.MAX_PARA_LEN = config["MAX_PARA_LEN"]

    def format_diff(self, fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5, *, charset='utf-8'):
        self._make_prefix()

        # change tabs to spaces before it gets more difficult after we insert
        # markup
        fromlines, tolines = self._tab_newline_replace(fromlines, tolines)

        # create diffs iterator which generates side by side from/to data
        if context:
            context_lines = numlines
        else:
            context_lines = None
        diffs = difflib._mdiff(fromlines, tolines, context_lines, linejunk=self._linejunk,
                               charjunk=self._charjunk)

        return list(diffs)


html1_doc = open("./cases/case3.pdf.html").read()
html2_doc = open("./cases/case4.pdf.html").read()
# html1_doc = open("./cases/case5.pdf.html").read()
# html2_doc = open("./cases/case6.pdf.html").read()


def extract_spans(html_doc):
    """
    该方式抽取的抽出来的正文 格式上比较粗略
    :param html_doc:
    :return:
    """
    contents = []
    soup = BeautifulSoup(html_doc, "html.parser")
    #     soup.find_all(class_=re.compile("itl"))
    #     text = soup.find_all('span',class_="left-del-text")
    alltext = soup.find("div", id="page-container")

    # pf 页
    pages = alltext.find_all("div", class_=re.compile("pc"))
    # print(pages)
    for page in pages:
        sections = page.find_all("div", recursive=False)
        for sec in sections:
            # print(sec.text)
            contents.append(sec.text)
            # print("---")
    return contents


contents1 = extract_spans(html1_doc)
contents2 = extract_spans(html2_doc)


def get_lenofline(text_paras):
    """
    获取每个段落的长度
    """
    lenoflines = []
    return [len(text_paras[i]) for i in range(len(text_paras))]


right_lens = get_lenofline(contents2)
left_lens = get_lenofline(contents1)


def sum_lens(lens):
    new_lens = []
    for i in range(len(lens)):
        new_lens.append(sum(lens[0:i+1]))
    return new_lens


left_indexes = sum_lens(left_lens)
right_indexes = sum_lens(right_lens)

differ = DocxDiff()
# 字string对比
diff_result = differ.format_diff("".join(contents1), "".join(contents2))


def listdiff(diffs):

    Ldiffs = []
    new_diffs = []
    for item in diffs:
        l = item[0][1]
        r = item[1][1]
        if "\x00-" in l and "\00+" in r:
            l = l.replace("\x00-", "").replace("\x01", "")  # \x04 mod
            r = r.replace("\x00+", "").replace("\x01", "")  # \x04 mod
            new_diffs.append((l, r, "\x04"))
        elif "\x00-" in l:
            l = l.replace("\x00-", "").replace("\x01", "")  # \x03  del
            new_diffs.append((l, r, "\x03"))
        elif "\x00+" in r:
            r = r.replace("\x00+", "").replace("\x01", "")  # \x02 add
            new_diffs.append((l, r, "\x02"))
        else:
            new_diffs.append((l, r, "0"))
        cur = 0
    #     print(new_diffs)
    cur = None
    for d in new_diffs:
        c2 = d[2]
        c0 = d[0]
        c1 = d[1]
        #         if c2 in ["\x02","\x03","\x04"]:
        if cur != c2:
            cur = c2
            if cur == "\x02":
                #                 Ladds.append([c0,c1,"add"])
                Ldiffs.append([c0, c1, "add", len(Ldiffs)])
            elif cur == "\x03":
                #                 Ldels.append([c0,c1,"del"])
                Ldiffs.append([c0, c1, "del", len(Ldiffs)])
            elif cur == "\x04":
                #                 Lchgs.append([c0,c1,"mod"])
                Ldiffs.append([c0, c1, "mod", len(Ldiffs)])
            else:
                Ldiffs.append([c0, c1, "0", len(Ldiffs)])
        else:
            if cur == "\x02":
                #                 Ladds[-1][0] += c0
                #                 Ladds[-1][1] += c1
                Ldiffs[-1][0] += c0
                Ldiffs[-1][1] += c1
            elif cur == "\x03":
                #                 Ldels[-1][0] += c0
                #                 Ldels[-1][1] += c1
                Ldiffs[-1][0] += c0
                Ldiffs[-1][1] += c1
            elif cur == "\x04":
                #                 Lchgs[-1][0] += c0
                #                 Lchgs[-1][1] += c1
                Ldiffs[-1][0] += c0
                Ldiffs[-1][1] += c1
            else:
                Ldiffs[-1][0] += c0
                Ldiffs[-1][1] += c1
    return Ldiffs


Ldiffs = listdiff(diff_result)


def append_chars(Ldiffs, left_indexes, right_indexes, c0_index, c1_index, c0, c1):
    #     print(c1_index)
    Ldiffs[-1][0][-1] += c0  # left
    Ldiffs[-1][1][-1] += c1  # right
    if c0_index in left_indexes:
        Ldiffs[-1][0].append("")
    if c1_index in right_indexes:
        Ldiffs[-1][1].append("")


def listdiff(diffs, left_indexes=[], right_indexes=[]):
    """
    字符级别diff转为line级别的，合同相同类型的char
    """
    Lchgs = []
    Ladds = []
    Ldels = []
    Ldiffs = []

    Ldiffs = []
    new_diffs = []

    # 格式修改
    for item in diffs:
        l_index = item[0][0]
        r_index = item[1][0]
        l = item[0][1]
        r = item[1][1]
        if "\x00-" in l and "\00+" in r:
            l = l.replace("\x00-", "").replace("\x01", "")  # \x04 mod
            r = r.replace("\x00+", "").replace("\x01", "")  # \x04 mod
            le = (l_index, l)
            re = (r_index, r)
            new_diffs.append((le, re, "\x04"))
        elif "\x00-" in l:
            l = l.replace("\x00-", "").replace("\x01", "")  # \x03  del
            le = (l_index, l)
            re = (r_index, r)
            new_diffs.append((le, re, "\x03"))
        elif "\x00+" in r:
            r = r.replace("\x00+", "").replace("\x01", "")  # \x02 add
            le = (l_index, l)
            re = (r_index, r)
            new_diffs.append((le, re, "\x02"))
        else:
            le = (l_index, l)
            re = (r_index, r)
            new_diffs.append((le, re, "0"))
        cur = 0
    #     print(new_diffs)
    cur = None

    # 再次格式修改  chars-->lines
    for d in new_diffs:
        c2 = d[2]

        c0_index = d[0][0]
        c0 = d[0][1]
        c1_index = d[1][0]
        c1 = d[1][1]
        #         if c2 in ["\x02","\x03","\x04"]:
        if cur != c2:
            cur = c2
            if cur == "\x02":
                #                 Ladds.append([c0,c1,"add"])
                Ldiffs.append([[c0], [c1], "add", len(Ldiffs)])
            elif cur == "\x03":
                #                 Ldels.append([c0,c1,"del"])
                Ldiffs.append([[c0], [c1], "del", len(Ldiffs)])
            elif cur == "\x04":
                #                 Lchgs.append([c0,c1,"mod"])
                Ldiffs.append([[c0], [c1], "mod", len(Ldiffs)])
            else:
                Ldiffs.append([[c0], [c1], "0", len(Ldiffs)])
        else:  # cur == c2
            #             if c0_index in left_indexes:
            #                 pass

            #             if c1_index in right_indexes:
            #                 pass

            if cur == "\x02":
                #                 Ladds[-1][0] += c0
                #                 Ladds[-1][1] += c1
                #                 Ldiffs[-1][0][-1] += c0
                #                 Ldiffs[-1][1][-1] += c1
                append_chars(Ldiffs, left_indexes, right_indexes,
                             c0_index, c1_index, c0, c1)
            elif cur == "\x03":
                #                 Ldels[-1][0] += c0
                #                 Ldels[-1][1] += c1
                #                 Ldiffs[-1][0][-1] += c0
                #                 Ldiffs[-1][1][-1] += c1
                append_chars(Ldiffs, left_indexes, right_indexes,
                             c0_index, c1_index, c0, c1)
            elif cur == "\x04":
                #                 Lchgs[-1][0] += c0
                #                 Lchgs[-1][1] += c1
                #                 Ldiffs[-1][0][-1] += c0
                #                 Ldiffs[-1][1][-1] += c1
                append_chars(Ldiffs, left_indexes, right_indexes,
                             c0_index, c1_index, c0, c1)
            else:
                #                 Ldiffs[-1][0][-1] += c0
                #                 Ldiffs[-1][1][-1] += c1
                append_chars(Ldiffs, left_indexes, right_indexes,
                             c0_index, c1_index, c0, c1)
    return Ldiffs


Ldiffs = listdiff(diff_result, left_indexes, right_indexes)
for e in Ldiffs:
    print(e)
