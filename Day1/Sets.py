myset = {"apple", "banana", "cherry"}
print(myset)


mixed_set = {"apple", "banana", "cherry", True, 1, 2}
# The values True and 1 are considered the same value in sets, and are treated as duplicates
# it keeps True & ignore 1
print(mixed_set)

# The values False and 0 are considered the same value in sets, and are treated as duplicates
# it keeps False & ignore 0
mixed_set = {"apple", "banana", "cherry", False, True, 0}
print(mixed_set)

# set() Constructor
# we can use the set() constructor to make a set.
mixed_set= set(("apple", "banana", "cherry")) # note the double round-brackets
print(mixed_set)

# Access Items

# using in keyword
for x in mixed_set:
  print(x)
  
# Change Items
# Once a set is created, 
# you cannot change its items, but you can add new items.

# Add Items
mixed_set.add("orange") # add at the starting position
print(mixed_set)

# Add Sets
tropical = {"pineapple", "mango", "papaya"}
mixed_set.update(tropical)
print(mixed_set)

# Add Any Iterable
my_list = ["kiwi", "blueberry"]
mixed_set.update(my_list)
print(mixed_set)

# Remove Item
# To remove an item in a set, use the remove(), 
# or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
mixed_set.remove("banana")
mixed_set.discard("banana")
print(mixed_set)

# Sets are unordered, so when using the pop() method, 
# you do not know which item that gets removed.
popped_item = mixed_set.pop()
print(popped_item) 
print(mixed_set)

# The clear() method empties the set
# mixed_set.clear()

# The del keyword will delete the set completely

# Loop Items
for x in mixed_set:
  print(x)
  
# Join set1 and set2 into a new set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# You can use the | operator instead of the union() method, 
# and you will get the same result

# The  | operator only allows you to join sets with sets, 
# and not with other data types like you can with the union() method.
set3 = set1.union(set2) # The result will be a set.
# or
set3 = set1 | set2
print(set3)
# You can join multiple sets

# Update 
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

# Difference
# The difference() method will return a new set that will contain only 
# the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# You can use the - operator instead of the difference() method, 
# and you will get the same result.
set3 = set1.difference(set2) # allows other datatypes
# or 
set3 = set1 - set2 # only allows join sets with sets
print(set3)

# The difference_update() method will also keep the items from the first set 
# that are not in the other set, but it will change the original set instead
# of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) # {'banana', 'cherry'}

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
# or 
set3 = set1 ^ set2
print(set3) # {'google', 'banana', 'microsoft', 'cherry'}

# symmetric_difference() returns a new set without modifying the original set.
# symmetric_difference_update() updates the original set and does not return anything.

# Initial Sets:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# After symmetric_difference():
new_set = set1.symmetric_difference(set2)
# new_set = {1, 2, 4, 5}
# set1 remains {1, 2, 3}

# After symmetric_difference_update():
set1.symmetric_difference_update(set2)
# set1 is now {1, 2, 4, 5}





