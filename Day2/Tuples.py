# Create a Tuple
my_tuple = ('A', 14, "Veena")
print(my_tuple)

# Tuple Length
print("Length :", len(my_tuple))

# Create Tuple With One Item

#NOT a tuple
m_tuple = ("apple")
print(type(m_tuple)) # 'str'

# To create a tuple with only one
# item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.
fruit1_tuple = ("apple",)
print(type(fruit1_tuple)) # 'tuple

# The tuple() Constructor
# note the double round-brackets
fruits = tuple(("apple", "banana", "cherry")) 
print(fruits)

# Accessing Elements
print(fruits[2])
print(fruits[-3])

# Update Tuple
# Convert tuple into list => make change => convert back to tuple
y = list(fruits)
y[1] = "kiwi"
fruits = tuple(y)
print(fruits)

# Add Items
y = list(fruits)
y.append("orange")
fruits = tuple(y)
print(fruits)

y = ("blueeberry",)
fruits += y
print(fruits)

# Remove Items 
y = list(fruits)
y.remove("apple")
fruits = tuple(y)
print(fruits)
# d_tuple = ("apple", "banana", "cherry")
# del d_tuple
# this will raise an error because the tuple no longer exists
# print(d_tuple)

# Unpacking a Tuple
(white, bloodRed, orange, blue) = fruits

print(white)
print(bloodRed)
print(orange)
print(blue)

# using Asterisk *
(white, *bloodRed, orange) = fruits # you can use * with any  
print(white)
print(bloodRed)
print(orange)

# Loop Through a Tuple
for x in fruits:
  print(x)
  
# Loop Through the Index Numbers
for i in range(len(fruits)):
  print(fruits[i])