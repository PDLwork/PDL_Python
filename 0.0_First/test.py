import sympy

#解方程 有限解
#定义变量
x=sympy.Symbol('x')
fx= ((1 / (sympy.sqrt(2 * sympy.pi) * x)) * sympy.exp(-1 / (2 * x ** 2))) - 3/4
#可求解直接给出解向量
y1=fx.evalf(subs={x:1.1})
# print(sympy.solve(fx,x))
print(y1)