# Exercise — Strongest Password

# Write a function that returns the strongest password from a list.

# Rules
# Password score:

# | Condition          | Points |
# | ------------------ | ------ |
# | length ≥ 8         | +2     |
# | contains uppercase | +1     |
# | contains digit     | +1     |


def strongest_password (passwords: list) -> str:

    best_password = ""
    best_score = -1

    for password in passwords:

        score = 0

        if len(password) >= 8: 
            score += 2

        for char in password:
            if char.isupper():
                score += 1
                break

        for char in password:
            if char.isdigit():
                score += 1
                break

        if score > best_score:  # update password
            best_score = score
            best_password = password

    return best_password


# create a list of words to test

if __name__ == "__main__":

    passwords = ["cat","hola123", "password1", "PassworD3"]

    print(strongest_password(passwords))
