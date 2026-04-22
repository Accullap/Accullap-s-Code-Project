import numpy as np 

def addition(x,y):
    return x+y

np.add = np.frompyfunc(addition, 2, 1)

k = np.addition([3, 4, 5],[1, 2, 3])


def multiply(x,y):
    return x*y 

np.multiply = np.frompyfunc(multiply, 2, 1)

j = np.array([7,8,9])
p = np.array([4,5,6])

def div(x,y):
    return x/y

np.div = np.frompyfunc(div, 2, 1)


def subtract(x,y):
    return x-y

np.subtract = np.frompyfunc(subtract, 2, 1)

print(np.subtract(j,p))
