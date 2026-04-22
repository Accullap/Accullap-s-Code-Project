import numpy as np 

def add(x, y):
    return x+y

np.add = np.frompyfunc(add, 2, 1)

k = np.add([3, 4, 5],[1, 2, 3])


def multiply(x, y):
    return x*y 

np.multiply = np.frompyfunc(multiply, 2, 1)

j = np.array([1,2,3])
p = np.array([4,5,6])

print(np.multiply(j, p))

