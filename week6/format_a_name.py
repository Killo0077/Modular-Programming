# Lab 6 - Value Returning Functios

# 1. Format a name

# Write a function that receives a first name and a surname and returns a single string
# with the surname followed by a comma and space and followed by the first name.

# def create_string(first, last):
#     return f"{last}, {first}"

# print(create_string ("Baena", "Pablo"))



def format_string(first: str, last : str) -> str:
    """
    Retruns a formatted name.
    
    Parameters:
        first (str): the person's first name
        last (str): the person's last name
        
    Returns: 
        str: name formatted as "lastname, firstname
        """
    name = f"{last}, {first}"
    return name

# print (format_string("Pablo", "Baena"))  

if __name__ == "__main__":
    result = format_string("Pablo", "Baena")
    print(result)