import numpy

list1 = [0, 5, 0]
list1 = numpy.array([[0, 5, 0],[0, -2, 0]])
action = numpy.argwhere(list1[1] == 0)[0][0]
print(action)