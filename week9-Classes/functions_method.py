# A method is a function defined inside a class/ Methods describe what the objec can do . 
# drive()
# honk()

#Example:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 

    def drive(self):
        print(f"The {self.make} {self.model} is driving!")

    def honk(self):
        print(f"The {self.make} {self.model} honks its horn!")

if __name__ == '__main__':
    # Creating an object of Car class
    my_car = Car("Toyota", "Corolla", 2020)

    # Calling methods on the object
    my_car.drive() # Output: The Toyota Corrolla is driving!
    my_car.honk() # Output: The Toyota Corrolla honks its horn!
