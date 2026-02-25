# Question 3: Type hint to return type hint to specify what datatype is expected as a parameter (if it has one)
# and what is returned


def welcome(name = "User") -> None:
    """
    Display a welcome message for a user.
    :param name: the name of the user logging in, default "User".
    """
    print(f"Welcome to you, {name}.")

welcome()
welcome("Pablo")