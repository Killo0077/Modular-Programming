# 4 – Lock an account?

# An IT Technician has been asked to develop a system to determine whether a user
# account should be locked after multiple failed login attempts.

# Write a function that receives:
# • Number of failed attempts (integer)
# • Maximum attempts allowed (integer)
# • Age of account in days (integer)
# Rules:
# • If age of the account is <7 days, add 2 to the maximum number of attempts
# • If failed attempts ≥ maximum allowed → lock the account
# Return:
# • A single boolean value
# o True if the account should be locked
# o False otherwise
# Sample usage might be:
# print(should_lock_account(5, 5, 30)) # True - Old account
# print(should_lock_account(5, 5, 6)) # False - Newer account


def lock_an_account (number : int, max: int, age: int) -> int:
    """
    :param number : number of failed attempts (integer)
    :param max: maximum attempts allowed (integer)
    :param age: Age of account in days (integer)
    """
        # If account is new than 2 days
    if age < 7:
        max = max + 2

    # check if account should be locked
    if number >= max:
        return True
    else:
        return False
    
if __name__ == "__main__":
    # print(lock_an_account(5,5,30))  # True - old account
    # print(lock_an_account(5,5,5))   #False - new account

    print(lock_an_account(5,5,8))  # True - old account
    print(lock_an_account(5,5,1))   #False - new account
                        # number / max / age