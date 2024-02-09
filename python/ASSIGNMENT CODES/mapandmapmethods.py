def square(x):
    return x**2
numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))