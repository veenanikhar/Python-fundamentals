#Looping Through a List

fruits = ["apple", "orange", "cherry"]
for x in fruits:
  print(x)
  
# Looping Through a String
for x in "Veena":
  print(x)
  
# break 
for x in fruits:
  print(x)
  if x == "orange":
    break
  
# continue 
for x in fruits:
  if x == "orange":
    break
  print(x)
  
# range()
for x in range(6):
  print(x)
  
# Else in For Loop
# The else keyword
# in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
# Nested Loops
adj = ["red", "big", "tasty"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
# for loops cannot be empty,
# but if you for some reason have a for loop with no content, put in the pass statement
# to avoid getting an error.
for x in [0, 1, 2]:
  pass