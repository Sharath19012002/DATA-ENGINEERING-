#example of lambda function
str1 = 'HexaforHexa'
upper = lambda string: string.upper()
print(upper(str1))

#Use of Lambda Function in Python:
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))


#Difference Between Lambda functions and def defined function:
def cube(y):
    return y * y * y
lambda_cube = lambda y: y * y * y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

#Python Lambda Function with List Comprehension:
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

#Python Lambda Function with if-else:
Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))
Min=lambda a,b:a if (a<b) else b
print(Min(1,2))

#Python Lambda with Multiple Statements:
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)

#Using lambda() Function with filter():
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

#Filter all people having age more than 18, using lambda and filter() function
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)

#Using lambda() Function with map():
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

#Using lambda() Function with reduce():
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)


































