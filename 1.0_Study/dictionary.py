print("————————————————————————————创建字典————————————————————————————")
#花括号{}创建
dictionary1 = {"张三": 95, "李四": 80, "王五": 59}
print(dictionary1)
print(type(dictionary1))

#用dict（）创建
dictionary2 = dict(name="赵四", scores=87)
print(dictionary2)

#空字典
dictionary3 = {}
dictionary4 = dict()
print(dictionary3)
print(dictionary4)

#字典元素获取
print("————————————————————————————字典元素获取————————————————————————————")
#直接通过键获取
dictionary1 = {"张三": 95, "李四": 80, "王五": 59}
print(dictionary1['张三'])
#print(dictionary1["陈六"])    #KeyError: '陈六'

#用内置get（）函数获取
print(dictionary1.get("张三"))
print(dictionary1.get("陈六"))    #None，和直接获取有区别，用内置get（）函数，当键不存在时不会报错
print(dictionary1.get("赵七", 99))    #若没有键，则返回设定值

#键判断、增、删、改
print("————————————————————————————键判断————————————————————————————")
dictionary1 = {"张三": 95, "李四": 80, "王五": 59}
print("张三" in dictionary1)
print("张三" not in dictionary1)

print("————————————————————————————键值对删除————————————————————————————")
dictionary2 = dict(name="赵四", scores=87, hobby="basketball")
del dictionary2["name"]     #删除指定键值对，似乎需要将键值用引号括起来
print(dictionary2)
dictionary2.clear()         #清空字典
print(dictionary2)

print("————————————————————————————键值对增加————————————————————————————")
dictionary1 = {"张三": 95, "李四": 80, "王五": 59}
dictionary1["陈六"] = 50
print(dictionary1)

print("————————————————————————————键值对修改————————————————————————————")
dictionary1["陈六"] = 100
print(dictionary1)

#字典提取
print("————————————————————————————字典提取————————————————————————————")
#键的提取
dictionary1 = {"张三": 95, "李四": 80, "王五": 59}
keys = dictionary1.keys()
print(keys)     #提取键
print(type(keys))
print(list(keys))   #将键转换成列表

#值的提取
values = dictionary1.values()
print(values)
print(type(values))
print(list(values))

#获取键值对
items = dictionary1.items()
print(items)
print(type(items))
print(list(items))      #转换之后的元素由元组组成

#字典遍历
print("————————————————————————————字典遍历————————————————————————————")
dictionary1 = {"张三": 95, "李四": 80, "王五": 59}
for items in dictionary1:
    print(items)
    print(dictionary1[items])

#字典进阶
print("————————————————————————————字典进阶————————————————————————————")
dictionary1 = {"张三": 95, "李四": 80, "张三": 59}
print(dictionary1)  #键不允许重复

dictionary1 = {"张三": 95, "李四": 95, "王五": 59}
print(dictionary1)  #制可以重复

#字典生成式
list1 = ["张三", "李四", "王五"]
list2 = [95, 80, 55]
dictionary2 = {keys:values for keys, values in zip(list1, list2)}
print(dictionary2)