# Question 4- Type hint to on parameter

def welcome(name:str = "User") -> None:
    """Displays a welcome message for a user.
    
    :param name: the name of the user logging in 
    """
    print(f"Welcome to you, {name}.")

welcome()
welcome("Pablo")