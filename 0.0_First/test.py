'''三引号注释
可以换行
#号键不能换行
'''

# a = 1
# b = 5               #加上注释
# if a < b:
#     print(b -a)
# else:
#     print(a -b)


'''自定义函数'''
def compair(number_a, number_b):
    if number_a < number_b:
        number_c = number_b - number_a
    else:
        number_c = number_a - number_b
    return number_c

c = compair(5, 1)
print(compair(20, 10))