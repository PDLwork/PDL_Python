import math

print(math)
print(id(math))
print(type(math))
print(math.pi)

'''两种引用模块区别,尤其是函数使用时调用的区别'''
'''引入模块其中一种功能'''
from module2 import fun1

print(fun1(6, 5, 6))

'''引入模块的全部功能'''
import module2
print(module2.fun1(4, 5, 6))
module2.hi()