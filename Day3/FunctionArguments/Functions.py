# Creating a Function
def my_function():
  print("Hello from a function")
  
# Calling a function
my_function()

# Function with arguments
def functionWithArg(fname):
  print("My name is", fname)

functionWithArg("Veena")

def functionWithMultiArg(fname, lname):
  print("My name is", fname, lname)

functionWithMultiArg("Veena", "Nikhar")

# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.

# This way the function will receive a 'tuple' of arguments, and can access the items accordingly

def functionUnArg(*kids):
  print("The youngest child is " + kids[2])

functionUnArg("T", "R", "V")