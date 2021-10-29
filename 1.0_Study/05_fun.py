print("------------------------函数使用--------------------------")

def findmax(x, y):
    if x > y:
        return x
    else:
        return y

a = 5
b = 10
c = findmax(a, b)
print("max = ", c)