## Cleaned version lock an account 


def lock_an_account (failed_attempts: int, max_attempts: int, age:int) -> int:
    """
    Determines if an account should be locked.
    
    :param failed_attempts: number of failed login attempts
    :param max_attempts: maximum attempts allowed
    :param age: account age in days
    :return: True if account should be locked, False otherwise
    """

    # New accounts get 2 extra attempts
    if age < 7:
        max_attempts += 2           ## <-- More clear than verion 1

    # Return the result of the comparison
    return failed_attempts >= max_attempts

if __name__ == "__main__":
    print(lock_an_account(5,5,30))  # True
    print(lock_an_account(5,5,6))   # False 