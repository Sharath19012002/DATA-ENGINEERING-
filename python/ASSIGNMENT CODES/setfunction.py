PYT = set()
PYT.add('s')
print("Letters are:", PYT)

# adding 'e' again
PYT.add('e')
print("Letters are:", PYT)
# adding 's' again
PYT.add('s')
print("Letters are:", PYT)

# set of letters
PYT = {'g', 'e', 'k'}

# adding 's'
PYT.add('s')
print("Letters are:", PYT)

# adding 's' again
PYT.add('s')
print("Letters are:", PYT)

# set of letters
PYT = {6, 0, 4}

# adding 1
PYT.add(1)
print('Letters are:', PYT)

# adding 0
PYT.add(0)
print('Letters are:', PYT)

# Python code to demonstrate addition of tuple to a set.
s = {'g', 'e', 'e', 'k', 's'}
t = ('f', 'o')
l = ['a', 'e']

# adding tuple t to set s.
s.add(t)

# adding list l to set s.
s.update(l)

print(s)



test_set = {1, 2, 3, 4}
test_set.clear()
print("After clear() on test_set:", test_set)

# set of letters
PYT = {"A", "B", "C"}
print('PYT before clear:', PYT)

# clearing vowels
PYT.clear()
print('PYT after clear:', PYT)

# Python program to demonstrate that copy
# created using set copy is shallow
first = {'g', 'e', 'e', 'k', 's'}
second = first.copy()
# before adding
print ('before adding: ')
print ('first: ', first)
print ('second: ', second)
# Adding element to second, first does not
# change.
second.add('f')
# after adding
print ('after adding: ')
print ('first: ', first)
print ('second: ', second)

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numbers)
# Deleting 5 from the set
numbers.discard(5)
# printing the resultant set
print(numbers)

myset = {'a', 1, "pyt", 2, 'b', 'abc', "Hexware", 8}

print(myset)

# Deleting a from the set
myset.discard("pyt")

# printing the resultant set
print(myset)

myset = {'a', 1, "pyt", 2, 'b', 'abc', "Hexware", 8}

print(myset)

# trying to Delete pytsfrom the set which is not there
myset.discard("pyts")

# printing the resultant set
print(myset)















