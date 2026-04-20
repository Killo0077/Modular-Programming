

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year



cars = [
    Car("Toyota", "Corolla", 2017),
    Car("Honda", "Civic", 2020),
    Car("Ford", "Focus", 2017),
    Car("BMw", "3 Series", 2019)
]




def get_oldest_car_year(cars_list):     
    return min(car.year for car in cars_list)



if __name__ == "__main__":
    for car in cars:
        print(car.make)

oldest_year = get_oldest_car_year(cars)
print("Oldest car year: ", oldest_year)
