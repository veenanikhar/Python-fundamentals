# Strings are Arrays
name = "Veena"
print(name[1])

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check if Not
print("expensive" not in txt)

# String length
print(len(name))

b = "Hello, World!"
print(b[2:5]) # 5 not included

#Slice From the Start
print(b[:5])

#Slice To the End
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#upper case
print(b.upper())

#lower case
print(b.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
print(a.split(",")) # returns ['Hello', ' World!']
