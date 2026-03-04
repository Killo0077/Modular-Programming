# 5 - Password Strength Scoring Function

# A Cybersecurity Technician has been asked to develop a system to evaluate the
# strength of user passwords before allowing account creation.
# Write a function that receives:
# • password (string)
# • minimum length (integer)
# The function should return a single integer score based on:
# • +2 points if password length ≥ minLength
# • +1 point if it contains at least one uppercase letter
# • +1 point if it contains at least one digit
# • +1 point if it contains at least one punctuation mark
# Return the final score (single integer).
# Note: the following code might be useful
# score = 0
# has_punc = False
# for k in range(len(password)):
# if password[k] in string.punctuation:
# has_punc = True
# if has_punc:
# score += 1
# Recall: string.punctuation contains all the punctuation marks in English.


import string



def password_strength (password: str, minimun_length: int) -> int:
    """
    Calculates the strength score of a password.
    
    :param password: the password to evaluate
    :param minimum_length: minimum required length
    :return: score of the password
    """
    score = 0

    if len(password) >= minimun_length:
        score += 2

    for char in password:
        if char.isupper():
            score += 1
            break
    for char in password:
        if char.isdigit():
            score +=1
            break
    for char in password:
        if char in string.punctuation:
            score += 1
            break
    
    return score

if __name__ == "__main__":
    password = "GamesofThrones"
    minimum_length = 8

    print(password_strength(password, minimum_length))