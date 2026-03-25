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

if __name__ == '__main__':
    my_phone= Phone("Apple","13",18)

    my_phone.new_storage(128)

    print(my_phone.model)
    print(my_phone.storage)
    
