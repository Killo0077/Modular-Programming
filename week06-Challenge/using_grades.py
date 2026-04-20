import grades

# if __name__ == "__main__":
#     print (grades.level17_grade(60))
#     print (grades.level18_grade(60))


#=======================================================================================
# Read the assessment mark
# Write a function that asks the user for a number (exam mark) between 0 and 100 and return
# that number.
# Add code to call this function in if/main.

def get_mark() -> int:
    """
    Ask the user for an exam mark.
    
    :return: exam mark entered by the user
    """

    mark = int(input("What is your grade? "))
    return mark

# if __name__ == "__main__":          #<<-- Only return number input by user
#     mark = get_mark()
#     print(mark)


# Read the degree level
# Write a function to ask the user for, and return, the level of their degree ie. 7 or 8.
# Add code to call this function in if/main.

def degree_level() -> int:
    """
    Ask the user what is the degree level.
    :return: Definicion grade from level selected.
    """
    degree = int(input("What is your degree: "))

    return degree

# if __name__ == "__main__":
#     degree = degree_level()
#     print(degree )


# Display the descriptive grade
# Write a function that receives an exam mark and a degree level, and returns the descriptive
# grade, using either the level7_grade() or level8_grade().

def descriptive_grade (mark: int, level: int) -> str:
    """Returns the descritive grade based on mark and degree level.
    
    :param mark: exam mark (0-100)
    :param level: degree level (7 or 8)
    :return: grade description
    """

    if level == 7: 
        return grades.level7_grade(mark)
    elif level == 8:
        return grades.level8_grade(mark)
    else:
        return "Invalid Degree level"
    
if __name__ == "__main__":
    mark = get_mark()
    level = degree_level()
    grade = descriptive_grade(mark, level)

    print("Your Grade is: ", grade)



