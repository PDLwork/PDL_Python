import numpy

list1 = numpy.array([[5, 6, 1, 3],[0, 1, 2, 3]])
list2 = list(list1[1])
print(list1)
print(list2)
print(list1[1])
print(type(list1[1]))
print(numpy.argwhere(list1[0] == 5 )[0][0])