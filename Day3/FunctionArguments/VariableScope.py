x = 200 # Global variable

def myfunc1():
  x = 300 # local variable
  print(x)

myfunc1()

# Function Inside Function
def myfunc2():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc2()

# Global Keyword
def myfunc3():
  global x
  x = 300 # update global variable 
myfunc3()
print(x)

# Nonlocal Keyword
