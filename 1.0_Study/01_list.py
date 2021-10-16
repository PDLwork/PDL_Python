#列表升序排序,将原列表进行排序
print("————————————————————————————列表升序排序————————————————————————————")
list1 = [55, 45, 30, 99]
print("排序前列表", list1, id(list1))
list1.sort()
print("升序排序后列表", list1, id(list1))

#列表降序排序,将原列表进行排序
print("————————————————————————————列表降序排序————————————————————————————")
list2 = [55, 45, 30, 99]
print("排序前列表", list2, id(list2))
list2.sort(reverse=True)
print("降序排序后列表", list2, id(list2))
list2.sort(reverse=False)
print("升序排序后列表", list2, id(list2))

#列表升降序排序,生成新的列表
print("————————————————————————————内置函数sorted()排序————————————————————————————")
list3 = [10, 99, 55, 65, 88]
new_list1 = sorted(list3)
new_list2 = sorted(list3, reverse=True)
print("原列表", list3)
print("升序列表", new_list1)
print("降序列表", new_list2)

#列表生成式生成列表
print("————————————————————————————列表生成式————————————————————————————")
list4 = [i for i in range(1, 11)]
list5 = [i*2 for i in range(1, 11)]
list6 = [i for i in range(2, 21, 2)]
print(list4)
print(list5)
print(list6)