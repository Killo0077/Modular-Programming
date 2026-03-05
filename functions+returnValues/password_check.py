# Exercise — Password Check

# Write a function that checks if a password is valid.

# Rules

# A password is valid if:

# 1️⃣ Length at least 8 characters
# 2️⃣ Contains at least one uppercase letter
# 3️⃣ Contains at least one digit

# If all conditions are true → return True
# Otherwise → return False

def valid_password (password: str) -> bool:
    if len(password) < 8:
        return False
    
    has_upper = False
    has_digit= False

    for char in password:
        if char.isupper():
            has_upper = True

        if char.isdigit():
            has_digit = True

    return has_upper and has_digit

if __name__ == "__main__":
    print(valid_password("Password1"))  # True
    print(valid_password("password"))   # False