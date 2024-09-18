class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myFunc(self):
    print("Hello my name is", self.name + " . I am" , self.age + " year old.")
    
p1 = Person("Veena", 25)
p1.myFunc()

# Modify Object Properties
p1.age = 40

# Delete Object Properties
del p1.age

# Delete Objects
del p1