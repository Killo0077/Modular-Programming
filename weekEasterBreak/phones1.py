# Create a class called Phone with attributes

class Phone():
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

def upgrade_storage(self,new_storage):
    if new_storage > self.storage:
        self.storage = new_storage
    else:
        print("New storage must be greater than current")

def __str__(self):
    return f"{self.brand} {self.model} {self.storage} Gb."

if __name__ == '__main__':

    phone1 = Phone ("Apple", "iPhone 13", 128)
    phone2 = Phone ("Samsung", "Galaxy S21", 256)
    phone3 = Phone ("Apple", "iPhone 16", 128)

