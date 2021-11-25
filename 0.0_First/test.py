import numpy

R = numpy.array\
([
    [-1,    -1,    -1,    -1,    0,    -1],
    [-1,    -1,    -1,     0,   -1,   100],
    [-1,    -1,    -1,     0,   -1,    -1],
    [-1,     0,     0,    -1,    0,    -1],
    [ 0,    -1,    -1,     0,   -1,   100],
    [-1,     0,    -1,    -1,    0,   100]
])

maxindex = numpy.argmin(R[4]) 
print(maxindex)

print((R[0] == 0).all())