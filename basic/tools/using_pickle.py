# using pickle
# persistent object -- 序列化 对象
import pickle
f = open('testobject', 'wb')
x = "hahah"
pickle.dump(x, f)
f.close

# f = open('testobject', 'r')  # read
# x = pickle.load(f)
# print(x)
