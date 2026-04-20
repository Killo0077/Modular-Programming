# Return to functions that include parameters and use :param to explain each parameter making it easier to red and less error-prone


##Example###

def welcome (name = "User"):
    """
    Displays a welcome message for a user.
    :param name: the name of the user logging in, default "User". 
    """
    print(f"Welcome to you, {name}.")

welcome()
welcome("Pablo")