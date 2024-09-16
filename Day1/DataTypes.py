# variables
x = "veena"
y = 3
z = 4.5

print(type(x))
print(type(y))
print(type(z))

# List
my_list = [1, 2, 3, "Python"]
print(my_list)
my_list[0] = 12 # Modifying the first element
print(my_list) #[12, 2, 3, 'Python']

#Tuple

my_tuple = (1, 2, 3, "Python")
print(my_tuple)
# my_tuple[0] = 12 # Error! Tuples are immutable.

# Range
my_range = range(1, 10, 2)
print(list(my_range))
print(tuple(my_range))

# dict 
my_dict = {"name": "Veena Nikhar", "age": 25, "city": "Bangalore"}
print(my_dict)
print(my_dict["name"]) # Veena Nikhar

# Adding a new key-value pair
my_dict["country"] = "India"
print(my_dict)

# Changing the value
my_dict["age"] = 26
print(my_dict)

# Set
my_set = {1,2,3,3,4}
print(my_set) # Duplicates are removed: output ->{1, 2, 3, 4}

# Frozenset
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)
# my_frozenset.add(5) # Error! Frozensets are immutable.

