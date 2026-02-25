# Part E- Modules

# A module is a Python file that contains functions for us to use. Hence functions.py is a module.


def welcome(name:str="User") -> None:
    """
    Display a welcome message for a user.
    
    :param name: the name of the user logging in
    """

    print(f"Welcome to you, {name}.")

    if __name__ == '__main__':
        welcome()
        welcome("Fred")