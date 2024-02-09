my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
# add(element)
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# update(iterable)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)
# remove(element)
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# pop()
my_set = {1, 2, 3, 4}
popped_element = my_set.pop()
print(popped_element)
print(my_set)
# union(iterable)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
# Alternatively: union_set = set1 | set2
print(union_set)
# intersection(iterable)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
# Alternatively: intersection_set = set1 & set2
print(intersection_set)
# difference(iterable)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
# Alternatively: difference_set = set1 - set2
print(difference_set)