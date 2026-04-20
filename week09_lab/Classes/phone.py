# Week 9 Lab Classes

class Phone():
    def __init__(self, brand, model, storage):
        self.brand = brand 
        self.model = model 
        self.storage = storage

    def new_storage(self, new_storage):
        if new_storage > self.storage:
            self.storage = new_storage 
        else:
            print("New storage must be greater than current")

    def __str__(self):
        return f"{self.brand} {self.model} {self.storage}Gb"
    
    def __eq__(self, other):
        return(
            self.brand == other.brand and 
            self.model == other.model and 
            self.storage == other.storage
        )
    

if __name__ == '__main__':
    # my_phone= Phone("Apple","13",18)

    # my_phone.new_storage(128)

    # print(my_phone.model)
    # print(my_phone.storage)
    phone1 = Phone("Apple", "Iphone 13", 128)
    phone2 = Phone("Samsung", "Galaxy S21", 256)
    phone3 = Phone("Apple", "Iphone 13", 128)

    # print(phone1)
    # print(phone2)
    # print(phone3)
    print(phone1 == phone2) # True
    print(phone1 == phone3) # False
    # phone1.new_storage(512)
    # print("Phone 1 has update memory",phone1)
    
    
