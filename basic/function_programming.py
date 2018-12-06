# function_programming


def f(x):
	return x % 2 != 0 and x % 3 != 0

print (filter(f,range(2,25)))


seq = range(8)
def  add(x,y): return x + y
print (map(add,seq,seq))

def cube(x): return x*x*x

print (map(cube,range(1,11)))


reportDataToal = dict(map(lambda x: (x, x), seq))
print (reportDataToal)


pendingNodes = []

pendingNodes.append("1")
pendingNodes.append(2)
nodes = list(pendingNodes)
print (pendingNodes)
print (nodes)