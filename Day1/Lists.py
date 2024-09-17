my_list = [1, 2, 3, "Python"]

# Creating a List
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'Python'

# Accessing Elements
print(my_list[-1])  # Output: 'Python' (last element)
print(my_list[-2])  # Output: 3 (second-to-last element)

# List Slicing
print(my_list[1:3]) # Output: [1, 2]

print(my_list)
my_list[0] = 12 # Modifying the first element
print(my_list) #[12, 2, 3, 'Python']

# Heterogeneous Data
mixed_list = [1, "Python", 3.14, [10, 20]]
print(mixed_list)

# Dynamic Size
mixed_list.append('A')
print(mixed_list)

# insert & pop from particular index
mixed_list.insert(2, "120")
print(mixed_list)

# Access the inner list at index 3
inner_list = mixed_list[4]

# Pop the value 10 from the inner list 
popped_value = inner_list.pop(0)
print(popped_value)
print(mixed_list)

# Loop Through a List
for x in my_list:
  print(x, end=' ')
  
# Loop Through the Index Numbers
for i in range(len(my_list)):
  print(my_list[i])
  

# Case Insensitive Sort
alphabates = ["o", "B", "k", "e", "A"]
# alphabates.sort()
print(alphabates)


# if you want a case-insensitive sort function, 
# use str.lower as a key function
alphabates.sort(key = str.lower)
print(alphabates)

alphabates = alphabates[2:] + alphabates[0:2]
print(alphabates)

# Reverse Order
alphabates.reverse()
print(alphabates)

# Copy Lists
# Use the copy() method
copy_Alpha = alphabates.copy()
print(alphabates)

# Use the list() method
list_alpha = list(alphabates)
print(alphabates)