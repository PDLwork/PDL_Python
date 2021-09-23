#元组的创建
print("————————————————————————————————元组的创建——————————————————————————————")
#小括号创建
tuple1 = ("Python", 123, "hello")
print(tuple1, type(tuple1))

#小括号可以省略
tuple2 = "hello world", 789, 56.2
print(tuple2, type(tuple2))

#单独元素时后面需要逗号，否则会被误认为别的类型
tuple3 = "Are you OK?",
print(tuple3)

#使用内置函数创建(里面似乎有两个括号)
tuple4 = tuple(("Python", 56))
print(tuple4)

#创建空元组
tuple5 = ()
tuple6 = tuple()
print(tuple5, tuple6)

#可变序列与不可变序列
#可变序列可以对内容进行增删改
#可变序列：列表、字典
#不可变序列：字符串、元组
print("————————————————————————————————可变序列与不可变序列——————————————————————————————")
#可变序列改变内容，其ID地址不变
print("可变序列")
list1 = [10, "Hello World", 56.5]
print(list1, id(list1))
list1.append(56)    #在末尾增加元素，ID地址不变
print(list1, id(list1))

print("不可变序列")
string1 = "Hello"
string2 = string1 + "World"
string3 = "HelloWorld"
print(string2)
print(id(string1), id(string2), id(string3))

#元组内的对象不可变，但元组对象指向的对象可以变
print("————————————————————————————————元组进阶——————————————————————————————")
tuple7 = ("Python", 123, [10, 20])
print(tuple7[0], type(tuple7[0]), id(tuple7[0]))
print(tuple7[1], type(tuple7[1]), id(tuple7[1]))
print(tuple7[2], type(tuple7[2]), id(tuple7[2]))
#tuple7[2] = [20, 10]    #error
tuple7[2].append(30)
print(tuple7[2], type(tuple7[2]), id(tuple7[2]))

#元组的遍历
print("————————————————————————————————元组的遍历——————————————————————————————")
tuple1 = ("Python", 123, "hello", 56.5, 1000)
for item in tuple1:
    print(item)