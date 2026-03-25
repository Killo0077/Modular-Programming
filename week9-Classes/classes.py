# A class describe:
# Attributes- the data the object stores
# Methods - the funtions/actions the object can perform

# class - blueprints
# Object - the house built from the blueprints



class Car:
    def __init__(self, make, model , year):
        self.make = make
        self.model = model 
        self.year = year 
        

if __name__ == '__main__':
    my_car = Car("Toyota", "Corolla", 2020)

    print(my_car.make) #Output: Toyota
    print(my_car.model) #Output: Corolla

    my_car.model = 'C-HR' 


