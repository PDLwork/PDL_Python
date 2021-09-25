print("------------------------------字符串的驻留机制---------------------------")
#三个变量名不同，但字符串相同，指向同一地址
a = 'python'
b = "python"
c = '''python'''

print(a, id(a))
print(b, id(b))
print(c, id(c))

a = "hello$"
b = "hello$"
print(id(a))
print(id(b))
print(a == b)
print(a is b)