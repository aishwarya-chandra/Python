# Unordered → No index, items may appear in any order
# Unchangeable → You can’t change items once added, but you can add/remove items
# Unique → No duplicate elements allowed

my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}
#OR
my_set = set([1, 2, 2, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4}

#operations
a = {1, 2, 3}
b = {3, 4, 5}
a.add(4) 
print(a)
a.remove(4)      # Removes x (errors if missing)
print(a)
a.discard(3)     # No error if x is missing
print(a)
print(1 in b)    # checks membership
print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric diff → {1, 2, 4, 5}
print(a-a)     #empty set denoted by set()
