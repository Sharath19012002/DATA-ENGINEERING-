# Python program to demonstrate
# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


# Driver code (We call myFun() with only
# argument)
##myFun(10)


# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Hexa', lastname='Practice')
student(lastname='Practice', firstname='Hexa')


def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


# You will get correct output because
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")


# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'HexaforHexa')


# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Hexa', mid='for', last='Hexa')


# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love HexaforHexa'

    def f2():
        print(s)

    f2()


# Driver's code
f1()


# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x * x * x

cube_v2 = lambda x: x * x * x

print(cube(7))
print(cube_v2(7))


def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num ** 2


print(square_value(2))
print(square_value(-4))


# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


# Python program to demonstrate working
# of map.
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
