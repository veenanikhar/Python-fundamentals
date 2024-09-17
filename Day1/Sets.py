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