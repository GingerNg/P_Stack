import difflib

config = {
    "MAX_PARA_LEN":40
}

def convert_diffs(diffs):
    """
    转换diffs
    :param diffs:
    :return:
    """
    froms = []
    tos = []
    flags = []
    fsflags = []
    for diff in diffs:
        # print(diff)
        if diff[2]:
            flags.append(True)
            f_char = diff[0][1]
            t_char = diff[1][1]
            if "\x00-" in f_char and "\x00+" in t_char:
                fsflags.append("^")
            elif "\x00-" in f_char:
                fsflags.append("-")
            elif "\x00+" in t_char:
                fsflags.append("+")
        else:
            fsflags.append("&")
            flags.append(False)
        froms.append(diff[0][1])
        tos.append(diff[1][1])
    return froms,tos,fsflags,flags


class MyHtmlDiff(difflib.HtmlDiff):
    def __init__(self):
        super().__init__()
        self.MAX_PARA_LEN = config["MAX_PARA_LEN"]

    def _connect_char(self, str1, str2):
        str1 = str1.strip("\x01") + str2.strip("\x00+").strip("\x00^").strip("\x00-")
        return str1

    def _convert_flag(self,char,flag):
        if flag == "^":
            char = char.replace("\x00-", "\x00^").replace("\x00+", "\x00^")
        return char

    def combine(self, diffs):
        """
        按字比对后进行合并
        :param diffs:
        :return:
        """
        froms, tos, fsflags, flags = convert_diffs(diffs)
        f_paras = [froms[0]]
        t_paras = [tos[0]]
        f_flags = [flags[0]]
        # fs_flags = [fsflags[0]]
        for i in range(1, len(flags)):
            if len(f_paras[len(f_paras) - 1]) <= self.MAX_PARA_LEN:
                froms[i] = self._convert_flag(char=froms[i],flag=fsflags[i])
                tos[i] = self._convert_flag(char=tos[i], flag=fsflags[i])
                if fsflags[i] != fsflags[i - 1]:
                    f_paras[len(f_paras) - 1] = f_paras[len(f_paras) - 1] + froms[i]
                    t_paras[len(t_paras) - 1] = t_paras[len(t_paras) - 1] + tos[i]
                else:
                    # fsflags[i] == fsflags[i - 1]:
                    f_paras[len(f_paras) - 1] = self._connect_char(str1=f_paras[len(f_paras) - 1], str2=froms[i])
                    t_paras[len(t_paras) - 1] = self._connect_char(str1=t_paras[len(t_paras) - 1], str2=tos[i])

                # f_paras[len(f_paras)-1] = f_paras[len(f_paras)-1] + froms[i]
                # t_paras[len(t_paras) - 1] = t_paras[len(t_paras) - 1] + tos[i]
                f_flags[len(f_flags) - 1] &= flags[i]
            else:
                # f_paras[len(f_paras) - 1] = f_paras[len(f_paras) - 1].replace("\x01\x00-","").replace("\x01\x00^","")
                # t_paras[len(f_paras) - 1] = t_paras[len(t_paras) - 1].replace("\x01\x00+","").replace("\x01\x00^","")
                froms[i] = self._convert_flag(char=froms[i],flag=fsflags[i])
                tos[i] = self._convert_flag(char=tos[i], flag=fsflags[i])
                t_paras.append(tos[i])
                f_paras.append(froms[i])
                cur_flag = flags[i]
                f_flags.append(cur_flag)
        # f_paras[len(f_paras) - 1] = f_paras[len(f_paras) - 1].replace("\x01\x00-", "").replace("\x01\x00^", "")
        # t_paras[len(f_paras) - 1] = t_paras[len(t_paras) - 1].replace("\x01\x00+", "").replace("\x01\x00^", "")
        for i in range(len(f_flags)):
            yield ((i, f_paras[i].strip()), (i, t_paras[i].strip()), flags[i])

    def _collect_lines(self, diffs):
        """
        重写原生方法
        :param diffs:
        :return:
        """
        diffs = self.combine(diffs)
        return super()._collect_lines(diffs)

    def count_diff(self, text1, text2):
        """
        按字比对后统计
        :param text1:
        :param text2:
        :return:
        """
        htmldiffer = difflib.HtmlDiff()
        htmldiffer._make_prefix()
        text1, text2 = htmldiffer._tab_newline_replace(text1, text2)
        diffs = difflib._mdiff(fromlines=text1, tolines=text2)
        froms, tos, fsflags, flags = convert_diffs(diffs)
        flags = fsflags
        add_count = 0
        delete_count = 0
        change_count = 0
        pre_flag = flags[0]
        if pre_flag == "+":
            add_count += 1
        elif pre_flag == "-":
            delete_count += 1
        elif pre_flag == "^":
            change_count += 1
        for i in range(1, len(flags)):
            now_page = flags[i]
            if now_page == "+" and now_page != pre_flag:
                add_count += 1
            elif now_page == "-" and now_page != pre_flag:
                delete_count += 1
            elif now_page == "^" and now_page != pre_flag:
                change_count += 1
            pre_flag = now_page
        return {"add": add_count, "delete": delete_count, "change": change_count}


# def mydiff(text1,text2):
#     try:
#         d = MyHtmlDiff()
#         # diff = d.make_file(text1.split("\n"), text2.split("\n"))
#         diff = d.make_file(text1, text2)
#         print(diff)
#         # return prettify_diff_result(diff)
#     except Exception as e:
#         raise Exception("文件对比异常, err:%s" % e.__str__())
#
#
# def diff(text1, text2):
#     try:
#         d = difflib.HtmlDiff()
#         # diff = d.make_file(text1.split("\n"), text2.split("\n"))
#         diff = d.make_file(text1, text2)
#         print(diff)
#         # return prettify_diff_result(diff)
#     except Exception as e:
#         raise Exception("文件对比异常, err:%s" % e.__str__())


class Text_Diff(object):
    def __init__(self):
        self.MAX_PARA_LEN = config["MAX_PARA_LEN"]

    def text_diff(self, text1, text2):
        """
        文本比对
        :param text1:
        :param text2:
        :return:
        """
        htmldiffer = difflib.HtmlDiff()
        htmldiffer._make_prefix()
        text1, text2 = htmldiffer._tab_newline_replace(text1, text2)
        diffs = difflib._mdiff(fromlines=text1, tolines=text2)
        # if self._wrapcolumn:
        # diffs = htmldiffer._line_wrapper(diffs)
        # for diff in diffs:
        #     print(diff)
        # fromlist, tolist, flaglist = htmldiffer._collect_lines(diffs)
        # print(fromlist)
        return diffs

    def get_paras(self, diffs):
        """
        根据按字对比信息进行分段
        :param diffs:
        :return:
        """
        f_paras = []
        t_paras = []
        froms, tos, fsflags, flags = convert_diffs(diffs)
        flags = fsflags
        f_paras.append(froms[0])
        t_paras.append(tos[0])
        cur_flag = flags[0]
        f_flags = []
        f_flags.append(cur_flag)
        for i in range(1, len(flags)):
            if cur_flag == flags[i] and len(f_paras[len(f_paras) - 1]) <= self.MAX_PARA_LEN:
                f_paras[len(f_paras) - 1] = f_paras[len(f_paras) - 1] + froms[i]
                t_paras[len(t_paras) - 1] = t_paras[len(t_paras) - 1] + tos[i]
            else:
                f_paras.append(froms[i])
                t_paras.append(tos[i])
                cur_flag = flags[i]
                f_flags.append(cur_flag)
        # f_paras = [para.replace("\n","") for para in f_paras if para.strip("\n") != ""]
        # t_paras = [para.replace("\n","") for para in t_paras if para.strip("\n") != ""]
        print(f_paras)
        print(t_paras)
        print(f_flags)
        tmp_f = [f_paras[0]]
        tmp_t = [t_paras[0]]
        i = 1
        cur_flag = f_flags[0]
        while i < len(f_paras):
            if len(f_paras[i]) < 5:
                tmp_f[len(tmp_f) - 1] = tmp_f[len(tmp_f) - 1] + f_paras[i]
                tmp_t[len(tmp_t) - 1] = tmp_t[len(tmp_t) - 1] + t_paras[i]
            elif (len(tmp_f[len(tmp_f) - 1]) > len(f_paras[i]) and cur_flag == "&") and \
                    len(tmp_f[len(tmp_f) - 1]) + len(f_paras[i]) <= self.MAX_PARA_LEN:
                tmp_f[len(tmp_f) - 1] = tmp_f[len(tmp_f) - 1] + f_paras[i]
                tmp_t[len(tmp_t) - 1] = tmp_t[len(tmp_t) - 1] + t_paras[i]
            else:
                tmp_f.append(f_paras[i])
                tmp_t.append(t_paras[i])
                cur_flag = f_flags[i]
            i += 1
        # tmp_f.append(f_paras[len(f_paras)-1])
        # tmp_t.append(t_paras[len(t_paras)-1])
        f_paras = [para.replace("\n", "") for para in tmp_f if para.strip("\n") != ""]
        t_paras = [para.replace("\n", "") for para in tmp_t if para.strip("\n") != ""]
        print(f_paras)
        print(t_paras)
        return f_paras, t_paras

    def gen_diff_counts(self, text1, text2):
        """
        分段后比对，统计个数
        :param text1:
        :param text2:
        :return:
        """
        htmldiffer = difflib.HtmlDiff()
        htmldiffer._make_prefix()
        text1, text2 = htmldiffer._tab_newline_replace(text1, text2)
        diffs = difflib._mdiff(fromlines=text1, tolines=text2)
        add_count = 0
        beginwithadd = False
        endwithadd = False
        delete_count = 0
        beginwithdelete = False
        endwithdelete = False
        from_change_count = 0
        from_beginwithchange = False
        from_endwithchange = False
        to_change_count = 0
        to_beginwithchange = False
        to_endwithchange = False
        # to_lines = []
        # from_lines = []
        for diff in diffs:
            if diff[2]:
                to_line = diff[1][1]
                from_line = diff[0][1]
                # to_lines.append(to_line)
                # from_lines.append(from_line)
                beg = ""
                if "\x01" in to_line and "\x00" in to_line:
                    for i in range(1, len(to_line)):  # add change
                        if to_line[i - 1] == "\x00" and to_line[i] == "+" or to_line[i] == "^":
                            beg = to_line[i]
                            if beg == "+":
                                if i == 1:
                                    beginwithadd = True
                                else:
                                    beginwithadd = False
                            if beg == "^":
                                if i == 1:
                                    to_beginwithchange = True
                                else:
                                    to_beginwithchange = False
                        elif to_line[i] == "\x01":
                            if beg == "^":
                                if not to_endwithchange or not to_beginwithchange:
                                    to_change_count += 1
                                to_endwithchange = False
                                if i == len(to_line) - 1:
                                    to_endwithchange = True
                            if beg == "+":
                                if not beginwithadd or not endwithadd:
                                    add_count += 1
                                endwithadd = False
                                if i == len(to_line) - 1:
                                    endwithadd = True
                    if "+" not in to_line:
                        endwithadd = False
                    if "^" not in to_line:
                        to_endwithchange = False
                # else:
                elif to_line != "\n" and len(to_line) > 0:
                    endwithadd = False
                    to_endwithchange = False
                beg = ""
                if "\x01" in from_line and "\x00" in from_line:
                    for i in range(1, len(from_line)):  # delete
                        if from_line[i - 1] == "\x00" and from_line[i] == "-" or from_line[i] == "^":
                            beg = from_line[i]
                            if beg == "^":
                                if i == 1:
                                    from_beginwithchange = True
                                else:
                                    from_beginwithchange = False
                            if beg == "-":
                                if i == 1:
                                    beginwithdelete = True
                                else:
                                    beginwithdelete = False
                        elif from_line[i] == "\x01":
                            if beg == "^":
                                if not from_endwithchange or not from_beginwithchange:
                                    from_change_count += 1
                                from_endwithchange = False
                                if i == len(from_line) - 1:
                                    from_endwithchange = True
                            if beg == "-":
                                if not beginwithdelete or not endwithdelete:
                                    delete_count += 1
                                endwithdelete = False
                                if i == len(from_line) - 1:
                                    endwithdelete = True
                    if "-" not in from_line:
                        endwithdelete = False
                    if "^" not in from_line:
                        from_endwithchange = False
                # else:
                elif from_line != "\n" and len(from_line) > 0:
                    endwithdelete = False
                    from_endwithchange = False
            else:
                endwithdelete = False
                from_endwithchange = False
                to_endwithchange = False
                endwithadd = False
        return {"add": add_count, "delete": delete_count, "change": (from_change_count + to_change_count) / 2}


if __name__ == '__main__':
    text_diff = Text_Diff()
    text2 = "无限公司、乙方任意一方直接或间接减持断罪小学有限责任公司股权，甲方有权要求乙方提前履行差额支付义务。AB123345657人生如戏，戏如人生！*+-？、，。《》二、承诺期间F1M！乙方应《哈哈哈》"
    text1 = "有限公司、乙方任意一方直接或间接减持断罪小学有限责任公司股权，甲方有权要求乙方提前履行差额支付义务。二、承诺期间乙方应"
    # # text2 = "XXXXXX】联系人:【李四】电话：【0371"
    # # text1 = "XXXXXX】联系人:【李四】电话：【0755"
    diffs = text_diff.text_diff(text1=text1, text2=text2)
    # f_paras, t_paras = text_diff.get_paras(diffs)
    # print(len("有限公司、乙方任意一方直接或间接减持断罪小学有限责任公司股权，甲方有权要求乙方提前"))
    # print(diff(f_paras, t_paras))

    html_diff = MyHtmlDiff()
    htmldiffs = html_diff.combine(diffs)
    # print("----")
    # for diff in htmldiffs:
    #     print(diff)

    # mydiff(text1,text2)
