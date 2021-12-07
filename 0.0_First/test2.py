import numpy

Q = numpy.zeros((1, 4))
print(Q)
Q = numpy.row_stack([Q, [0, 0, 0, 0]])
Q = numpy.row_stack([Q, [0, 0, 0, 0]])
print(Q)