print("------------------------------字符串的驻留机制---------------------------")
#三个变量名不同，但字符串相同，指向同一地址（在交互模式下时有区别）
a = 'python'
b = "python"
c = '''python'''

print(a, id(a))
print(b, id(b))
print(c, id(c))

#字符串增加，合并
a = 'abc'
b = 'ab' + 'c'
c = ''.join('abc')
d = ''.join('ab' + 'c')
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))

print("------------------------------字符串查询---------------------------")
a = 'hello, hello world'

print(a.index('lo'))    #3
print(a.find('lo'))    #3
print(a.rindex('lo'))    #10
print(a.rfind('lo'))    #10

#print(a.index('a')) #ValueError: substring not found
print(a.find('a'))  #-1
#用index查询时如果字符串里面没有会报错，但是find不会

print("------------------------------字符串常用操作---------------------------")
#字符串的大小写转换
# str.upper()   把字符串所有字符都转成大写字母
# str.lower()   把所有字符串都转成小写字母
# str.swapcase()    把所有字符串中的大写字母转换成小写字母，把所有小写字母转换成大写字母
# str.capitalize()  把第一个字母转换成大写，其余转换成小写
# str.title()   把每一个单词的第一个字符转换成大写，其余部分为小写,可以用逗号隔开或者空格隔开
string1 = 'Hello World hello world HELLO WORLD'
print(string1.upper())
print(string1.lower())
print(string1.swapcase())
print(string1.capitalize())
print(string1.title())
print()

#字符串的内容对齐操作方法
#str.center(width[, fillchar])返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
#str.ljust(width[, fillchar])返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
#str.rjust(width[, fillchar])返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
#str.zfill(width)方法返回指定长度的字符串，原字符串右对齐，前面填充0。
string1 = 'Hello World'

#居中
print(string1.center(20))
print(string1.center(20, '*'))
print(string1.center(5, '*'))
print()

#左对齐
print(string1.ljust(20))
print(string1.ljust(20, '*'))
print(string1.ljust(5, '*'))
print()

#右对齐
print(string1.rjust(20))
print(string1.rjust(20, '*'))
print(string1.rjust(5, '*'))
print()

#右对齐，前面用0填充（凑个热闹）
print(string1.zfill(20))
print(string1.zfill(5))