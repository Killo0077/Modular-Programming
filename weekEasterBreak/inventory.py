# Create a class called Product with attributes

class Product() :
    def __init__(self,name, price, stock):
        self.name= name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("Sorry not enough quantity in stock")

    def restock(self, quantity):
        self.stock += quantity



if __name__ == '__main__':
    p = Product("Laptop", 1000, 10)

    p.sell(3)  
    print(p.stock) # 7

    p.restock(5)
    print(p.stock) #12
    

