import numpy
# scalar
one = numpy.matrix([[6, -9, 1], [4, 24, 8]]) 
print(one * 2)
#dot product
e0 = numpy.array([[1, 0], [0, 1]])
e1 = numpy.array([[6, -9, 1], [4, 24, 8]])
print(e0 @ e1)  # @ does dot product
e0 = numpy.array([[4, 3], [3, 2]])
e1 = numpy.array([[-2, 3], [3, -4]])
print(e0 @ e1)  # @ does dot product
#print(v@e0) @ does dot product
