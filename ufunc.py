import numpy as np 


# kinda useless: add, subtract, divide, multiply already by default in np´s ufunc library


def addition(x,y):
    return x+y

np.addition = np.frompyfunc(addition, 2, 1)

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



a = np.array([1,2,3,4,5,6,7,8,9,10, 33, 44, 55, 66, 77])

newa = np.lcm.reduce(a)


print(newa)



