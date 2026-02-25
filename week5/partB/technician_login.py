# Question 1: Technician Login Message



def technician_login(name:str):   ### Use str to "mark" error input name

    """Documentation: def Technician welcome login Message"""
    print("Welcome to the company")
    print(f"Nice to meet you {name}")
    print("Have a good day!!!\n")

technician_login("Luigi")
technician_login("Mario Bros")
technician_login("324")