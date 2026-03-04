# Lab 6 - Value Returning Functios

# 1. Format a name

# Write a function that receives a first name and a surname and returns a single string
# with the surname followed by a comma and space and followed by the first name.

def create_string(first, last):
    return f"{last}, {first}"

print(create_string ("Baena", "Pablo"))
