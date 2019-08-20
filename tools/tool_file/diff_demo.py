import difflib
"""
https://www.cnblogs.com/Jabe/p/8948125.html
"""
print(len("C\x00-E\x01O"))

test2 = ["CTO","CO",
         "将寻陪审团审理，并索赔超过欧元。当事人称，侵事件导致她退出了明尼苏达大学下秋",
         "季学期所有课程的学习，并寻求专业。",
         "募、数十个行业领域的探索”为目标，向全世界产业界传递2019年MEC边缘云商用加速",
         "战略计划，重磅发布边缘业务平台CUBE-Edge2.0和相关白皮书。同时，中国联通还与"]

test1 = ["CTO","CEO",
         "她将寻求陪审团审理，并索赔超过美金。当事人称，性侵事件导致她退出了明尼苏达大学秋",
         "募、数十个行业领域的探索”为目标，向全球产业界传递2019年MEC边缘云商用加速战",
         "略计划，重磅发布边缘业务平台CUBE-Edge2.0和相关白皮书。同时，中国联通还与西"]

text1 = "232323232"
text2 = "23232323"

signals = ["\x00+","\x00-","\x00^","\x01"]
["+","-","^","&"]
["in","pre","back","all"]

def gen_diff_counts(text1, text2):
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
    change_count = 0
    beginwithchange = False
    endwithchange = False
    for diff in diffs:
        print(diff)
        # print(diff[2])s
        if diff[2]:
            from_line = diff[0][1]
            to_line = diff[1][1]
            beg = ""
            if len(from_line) >3:
                for i in range(1,len(from_line)): # delete
                    if from_line[i-1] == "\x00" and from_line[i] == "-":
                        beg = from_line[i]
                        if i == 1:
                            beginwithdelete = True
                    if from_line[i] == "\x01" and beg == "-":
                        if not endwithdelete or not beginwithdelete:
                            delete_count += 1
                        else:
                            endwithdelete = False
                        beg = ""
                        if i == len(from_line) -1:
                            endwithdelete = True

            beg = ""
            if len(to_line) > 3:
                for i in range(1,len(to_line)): # add change
                    if to_line[i-1] == "\x00" and to_line[i] == "+" or to_line[i] == "^":
                        beg = to_line[i]
                        if i == 1:
                            if beg == "+":
                                beginwithadd = True
                            if beg == "^":
                                beginwithchange = True
                    if to_line[i] == "\x01":
                        if beg == "^":
                            if not endwithchange or not beginwithchange:
                                change_count +=1
                            if i == len(to_line) - 1:
                                endwithchange = True
                        if beg == "+":
                            if not beginwithadd or not endwithadd:
                                add_count += 1
                            if i == len(to_line) -1:
                                endwithadd = True
    return {"add": add_count, "delete": delete_count, "change": change_count}





# diffs = difflib._mdiff(fromlines=test1, tolines=test2)
# for diff in diffs:
#     # print(diff)
#     # print(diff[2])
#     if diff[2]:
#         f_line = diff[0][1]
#         t_line = diff[1][1]
#         # print(f_line)
#         # print(t_line)
#         if "-" in f_line and "+" in t_line:
#             print("^")
#         elif "-" in f_line and "\n" in t_line:
#             print("-")
#         elif "\n" in f_line and "+" in t_line:
#             print("+")
#     else:
#         print("&")

from pyquery import PyQuery as pq
def count_diff(text1,text2):
    htmldiffer = difflib.HtmlDiff()
    htmldiffer._make_prefix()
    text1, text2 = htmldiffer._tab_newline_replace(text1, text2)
    diffs = difflib._mdiff(fromlines=text1, tolines=text2)
    # fromlist, tolist, flaglist = htmldiffer._collect_lines(diffs)
    # fromlist, tolist, flaglist, next_href, next_id = htmldiffer._convert_flags(
    #     fromlist, tolist, flaglist, context=False,numlines=5)
    # print(fromlist)
    # print(tolist)
    # for i in range(len(fromlist)):
    #     doc1 = pq(fromlist[i])
    #     print(doc1.text())
    # for i in range(len(tolist)):
    #     doc2 = pq(tolist[i])
    #     print(doc2.text())


    # print(flaglist)
    # print(next_href)
    # print(next_id)
    flags = []
    types = []
    for diff in diffs:
        print(diff)
        # print(diff[2])
        if diff[2]:
            f_line = diff[0][1]
            t_line = diff[1][1]
            if "\x00^" in f_line:
                flags.append("^")
            if "\x00-" in f_line:
                # print("-")
                flags.append("-")
            if "\x00+" in t_line:
                # print("+")
                flags.append("+")
        else:
            flags.append("&")
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
    for i in range(1,len(flags)):
        now_page = flags[i]
        if now_page == "+" and now_page != pre_flag:
            add_count +=1
        elif now_page == "-" and now_page != pre_flag:
            delete_count +=1
        elif now_page == "^" and now_page != pre_flag:
            change_count +=1
        pre_flag = now_page
    return {"add":add_count,"delete":delete_count,"change":change_count}

print(gen_diff_counts(text1,text2))
# print(gen_diff_counts("".join(test1),"".join(test2)))





s = difflib.SequenceMatcher(None,a=test1, b=test2)
# print(s.get_matching_blocks())


"""
Where T is the total number of elements in both sequences, and
M is the number of matches, this is 2.0*M / T.
"""
# print(s.ratio())
# print(s.get_matching_blocks())


d = difflib.Differ() #创建Differ对象
diffs = d.compare(test1,test2)
# for diff in diffs:
#     print(diff)
# print(" ".join(list(diff)))

# test1 = "今天天气真好 \n 今天天气不好"
# test2 = "今天天气不错"

# d = difflib.HtmlDiff()
# diff = d.make_file(test1,test2)
# print(diff)

# print()


"""
统计result.html中
<span class="diff_sub"> </span>
标签个数
"""






