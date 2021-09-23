#集合的创建方式
print("——————————————————————集合的创建方式——————————————————————")
#花括号创建
set1 = {"hello", 5, 2, 3, 3, "world"}
print(set1)     #不能重复，输出无序
print(type(set1))

#内置函数set（）创建
#set里面可以是列表、元组
set2 = set(range(2, 10, 3))
print(set2)
print(type(set2))

#注意set函数的用法
set3 = set("python")
set4 = {"python"}
print(set3, set4)

#创建空集合
set5 = {}
print(type(set5))   #<class 'dict'>
set6 = set()
print(type(set6))   #<class 'set'>

#集合的判断、增、删、改
print("——————————————————————集合的判断——————————————————————")
set1 = set("python")
print("p" in set1)
print("p" not  in set1)

print("——————————————————————集合的增加——————————————————————")
set1 = set("python")
set1.add(10)    #增加一个元素
print(set1)

set1.update("world")    #增加多个元素
set1.update((100, 200, "world"))
print(set1)

print("——————————————————————集合的删除——————————————————————")
#remove删除指定元素不存在会异常
set1 = set("python")
print(set1)
set1.remove("p")
print(set1)
# set1.remove("w")    #KeyError: 'w'
# print(set1)

#discard删除指定元素不存在不会异常
set2 = {10, 20, 30, 40}
print(set2)
set2.discard(10)
print(set2)
set2.discard(50)
print(set2)

#pop删除任意元素(但是重复运行只删除那个元素，我猜是内部随机)
set3 = {10, 20, 30, 40}
set3.pop()
print(set3)
set3.clear()    #清空集合
print(set3)

print("——————————————————————集合的逻辑关系——————————————————————")
set1 = set("python")
set2 = set("world")
set3 = {1, 2, 3, 4}
set4 = {4, 3, 2, 1}
print(set1 != set2)
print(set3 == set4)
print()

#并集
print(set1 | set2)  # 集合a或b中包含的所有元素
print(set1.union(set2))
#交集
print(set1 & set2)  # 集合a和b中都包含了的元素
print(set1.intersection(set2))
#差集
print(set1 - set2)  # 集合a中包含而集合b中不包含的元素
print(set1.difference(set2))
#对称差集
print(set1 ^ set2)  # 不同时包含于a和b的元素
print(set1.symmetric_difference(set2))
print()

set5 = set("HELLO")
set6 = set("HEL")
print(set6.issubset(set5))      #判断set6是否是set5的子集
print(set5.issuperset(set6))    #判断set5是否是set6的超集
print(set5.isdisjoint(set6))    #判断set5与set6是否没有交集

print("——————————————————————集合生成式——————————————————————")
#列表生成式
list1 = [i*i for i in range(6)]
print(list1)
