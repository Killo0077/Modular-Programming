# Create a class called Laptop 

class Laptop():
    def __init__(self,brand, model, ram, price):
        self.brand= brand
        self.model = model
        self.ram = ram
        self.price = price

    def upgrade_ram(self, new_ram):
        if new_ram > self.ram:
            self.ram = new_ram
        else:
            print("The memory ram need to be bigger than current")

    def __str__(self):
        return f"{self.brand} {self.model} {self.ram}Gb, $ {self.price} "

    def __eq__(self,other):
        return(
            self.brand == other.brand and
            self.model == other.model and
            self.ram == other.ram and
            self.price == other.price 
        )


if __name__ == '__main__':
    laptop1 = Laptop("Asus", "prime", 500,1200)
    laptop2 = Laptop("Apple", "A1", 250, 2000)
    laptop3 = Laptop("Toshiba", "Satellite", 500, 1250)

    print(laptop1)
    print(laptop2)
    print(laptop3)

    laptop1.upgrade_ram(600)
    print(laptop1)
    print(laptop1 == laptop2)
    print(laptop2 == laptop3)
        