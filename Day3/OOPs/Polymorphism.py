# Define a class Car
class Car:
    # Constructor method to initialize brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to simulate the car's movement
    def move(self):
        print("Drive!")  # Cars drive


# Define a class Boat
class Boat:
    # Constructor method to initialize brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to simulate the boat's movement
    def move(self):
        print("Sail!")  # Boats sail


# Define a class Plane
class Plane:
    # Constructor method to initialize brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to simulate the plane's movement
    def move(self):
        print("Fly!")  # Planes fly


# Create instances of Car, Boat, and Plane classes
car1 = Car("Ford", "Mustang")          # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")    # Create a Boat object
plane1 = Plane("Boeing", "747")        # Create a Plane object

# Iterate over the instances and call their respective move() methods
for x in (car1, boat1, plane1):
    x.move()  # Calls the move() method for each object (Drive, Sail, Fly)
