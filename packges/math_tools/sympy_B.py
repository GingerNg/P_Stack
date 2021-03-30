# --------多项式求解--------
# 定义变量
x = sympy.Symbol('x')
fx = 5*x+4
# 使用evalf函数传值
y1 = fx.evalf(subs={x: 6})
print(y1)
