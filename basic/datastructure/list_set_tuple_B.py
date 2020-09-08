ss = set([1, 2, 1])
ss.add(1)
print(ss)

tuple([1, 2, 3, 1])  # 不可变

# The extended slice syntax is our_list[begin:end:step] .
our_list = [1, 2, 3]
reversed_list = our_list[::-1]
print(reversed_list)

a, b = (3, 2)
print(a)
a = b = c = 1
print(a)

a, b = b, a
print(a)

print([0] != [0, 1])
