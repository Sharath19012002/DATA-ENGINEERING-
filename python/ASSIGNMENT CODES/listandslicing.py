'''my_list = [1, 2, 3, 4, 5]
print(my_list)'''
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits[1:3])

#append
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

#extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

#insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

#remove
numbers = [1, 2, 3, 4, 3]
numbers.remove(3)
print(numbers)  # Output: [1, 2, 4, 3]

#pop
numbers = [1, 2, 3, 4]
popped_element = numbers.pop(2)
print(popped_element)  # Output: 3
print(numbers)  # Output: [1, 2, 4]

#index
numbers = [10, 20, 30, 20, 40]
index = numbers.index(20)
print(index)  # Output: 1