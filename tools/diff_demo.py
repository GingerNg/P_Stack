import difflib
"""
https://www.cnblogs.com/Jabe/p/8948125.html
"""

test1 = "我是谁啊"

test2 = "我是谁"

s = difflib.SequenceMatcher(None,a=test1, b=test2)

"""
Where T is the total number of elements in both sequences, and
M is the number of matches, this is 2.0*M / T.
"""
print(s.ratio())
# print(s.get_matching_blocks())

d = difflib.Differ() #创建Differ对象
diff = d.compare(test1,test2)



print(" ".join(list(diff)))



d = difflib.HtmlDiff()
diff = d.make_file(test1,test2)
# print(diff)

# print()