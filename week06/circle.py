# (a)- Circle

# Create a new file called circle.py.
# Write a function that receives the radius of a circle and returns the circumference of
# that circle, 2πr where π is math.pi in Python.
# Write a function that receives the radius of a circle and returns the area of that circle A
# = πr2
# Write a few lines of code that uses these functions in if/main block.


import math   ### Formula: 2 * π * r

def circumference (radius: float) -> float:
    """
    Returns the circumference of a cicle.
    
    :param radius: radius of the circle
    :return: circumference of the circle
    """

    result = 2 * math.pi * radius
    return result


def area (radius: float) -> float:      ### Formula: π * r²
    """
    Returns the area of a circle.
    
    :param radius: radius of the circle
    :return: area of the circle
    """

    result = math.pi * radius ** 2
    return result


if __name__ == "__main__":

    r = 5          ### <-- number just for test it

    print("Circumference: ", circumference(r))
    print("Area: ", area(r))
