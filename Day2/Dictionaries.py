# Creating Dictionary
my_dict = {
  "name": "Veena",
  "age": 25 
}

# Accessing Values
print("Age =",my_dict["age"])

# Adding or Updating Key-Value Pairs
my_dict["city"] = "Bangalore"  # Adding new key-value pair
my_dict["age"] = 30 # Output: {'name': 'Veena', 'age': 30, 'city': 'Bangalore'}

# Iterating Through a Dictionary

# Keys
for key in my_dict:
  print(key)

# Values
for value in my_dict.values():
  print(value)

# Key-Value Pairs:
for key, value in my_dict.items():
    print(key, value)

# items()
print(my_dict.items())

# get(key, default) : Returns the 
# value associated with the key or a default value if the key is not found.
print(my_dict.get("name"))        # Output: Alice
print(my_dict.get("gender", "N/A"))  # Output: N/A (since key 'gender' doesn't exist)


# Merging Two Dictionaries using the update() method
dict2 = {"gender": "Female"}
my_dict.update(dict2)
print(my_dict)

# Removing Key-Value Pairs
del my_dict["age"]  # Remove key 'age'
my_dict.pop("city")  # Remove key 'city'

# Checking if a Key Exists using in keyword
if "name" in my_dict:
  print("Key 'name' is present") # Output: Key 'name' is present

# Nested Dictionry
myfamily = {
  "child1" : {
    "name" : "T",
    "year" : 1984
  },
  "child2" : {
    "name" : "R",
    "year" : 1987
  },
  "child3" : {
    "name" : "V",
    "year" : 1999
  }
}

# Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
