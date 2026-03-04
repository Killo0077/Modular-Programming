# 6 - Password Generator

# Write a function generate_personalised_password(tv_show, singer, colour) that:
# Parameters:
# • tv_show: The name of the student's favourite TV show (a string).
# • singer: The name of the student's favourite singer (a string).
# • colour: The student's favourite colour (a string).
# Returns:
# A personalized password.
# Password Generation Rules:
# • Combine the first 3 letters of the TV show, first 2 letters of the singer, and the last 2
# letters of the colour.
# o Recall: use slicing here e.g. tv_show[:3] gets first 3 letters of the show
# • Include a random number between 1 and 9 at the end.
# • Include a random punctuation character (e.g., @, #, !) at the start
# • Convert some letters to uppercase to improve password strength using the given
# function. Do you understand it? This could be refactored to be done in one line but
# is written here in a longer way to facilitate understanding.


import random
import string


def randomise_case (text: str) -> str: 
    """ Randomly changes letters to uppercase or lowercase
    
    :param text: input string
    :return : string with random letter cases
    """
    new_text = ""

    for char in text:
        if random.randint(0,1) == 1:
            new_text += char.upper()
        else:
            new_text += char.lower()
    
    return new_text


def password_generator (tv_show: str, singer: str, color: str) -> str:

    #slicing parts of words
    part1 = tv_show [:3]
    part2 = singer [:2]
    part3 = color [:-2]

    base = part1 + part2 + part3

    #random letters
    base = randomise_case(base)

    symbol = random.choice(string.punctuation)

    number = str(random.randint (1,9))

    password = symbol + base + number

    return password


if __name__ == "__main__":

    password = password_generator ("Friends", "John", "Red")

    print(password)