student = {'name': 'John', 'age': 20, 'grade': 'B'}
print(student['name'])
# get(key, default)D
student = {'name': 'John', 'age': 20, 'grade': 'B'}
age = student.get('age', 'N/A')
print(age)  # Output: 20

# Using get with a key that doesn't exist
address = student.get('address', 'N/A')
print(address)  # Output: N/A

# keys()

student = {'name': 'John', 'age': 20, 'grade': 'B'}
all_keys = student.keys()
print(all_keys)

# values()

student = {'name': 'John', 'age': 20, 'grade': 'B'}
all_values = student.values()
print(all_values)

# items()
student = {'name': 'John', 'age': 20, 'grade': 'B'}
all_items = student.items()
print(all_items)