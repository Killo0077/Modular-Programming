# Exercise — Circle Diameter

# Write a function that returns the diameter of a circle.


def circle_diameter(radius: float) -> float:
    """
    Calculates the diameter of a circle.
    
    :param radius: radius of the circle
    :return: diameter of the circle
    """

    diameter = 2 * radius

    return diameter

if __name__ == "__main__":
    result = circle_diameter(5)

    print(result)