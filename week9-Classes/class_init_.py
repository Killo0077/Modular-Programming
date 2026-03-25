# The __init__ Method

class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

if __name__ == '__main__':
    my_car = Car("Toyota", "Corolla", 2020)

    # Accessing the attributes of the objects
    print(my_car.make) #Output Toyota
    print(my_car.model) #Output Corolla

    my_car.model = 'C-HR'