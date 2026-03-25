# The __str__ Method is a special method that controls what is shown when print an object.

class Car:
    def __init__(self, make , model, year):
        self.make = make
        self.model = model 
        self.year = year 

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
if __name__ == '__main__':
    #Creating an object of Car class
    my_car = Car("Toyota", "Corolla", 2020)

    # Printing the object
    print(my_car) # Output: 2020 Toyota Corolla