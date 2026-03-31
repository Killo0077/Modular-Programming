# Create a class Account with attributes:


class Account():
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance")

    def __str__(self):
        return f"{self.owner} {self.balance}$"
    
    def __eq__(self,other):
        return(
            self.owner == other.owner and
            self.balance == other.balance
        )
    
    def transfer(self, other, amount):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
        else:
            print("Not enough balance to transfer")



if __name__ == '__main__':
    account1 = Account("John", 2300)
    account2 = Account("Mary", 1500)

    account1.transfer(account2, 500)
    
    print(account1)
    print(account2)

    print(account1 == account2)