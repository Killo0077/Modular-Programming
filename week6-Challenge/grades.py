# ### Week 6 Challenge / Paris

# ## Create a grades module

# Create a Python file called grades.py
# To this file add a function called level7_grade() that receives a number and returns the
# grade represented by that number i.e. "DT (Distinction)", "M1 (Merit, Grade 1)" etc. as
# determined by the following table

# DT      Distinction         70-100 %
# M1      Merit, Grade 1      60-69%
# M2      Merit, Grade 2      50-59%  
# PS      Pass                40-49%
# FL      Fail                0-39%

def level7_grade (mark: int) -> str:
    """
    Returns the level 7 grade for a given mark.
    
    :param mark: exam mark (0-100)
    :retun: grade description
    """

    if mark >= 70:
        return "DT (Distintion)"
    elif mark >=60:
        return "M1 (Merit, Grade 1)"
    elif mark >= 50:
        return "M2 (Merit, Grade 2)"
    elif mark >= 40:
        return "PS (Pass)"
    else:
        return "FL (Fail)"
    
# if __name__ == "__main__":
#     print (level7_grade(45))         
#     print (level7_grade(85))
#     print (level7_grade(55))


#=================================================================================#
# To this file add a function called level8_grade() that receives a number and returns the
# grade represented by that number i.e. "H1 (First Class Honours)", "2.1 (Second Class
# Honours, Grade 1)" etc. as determined by the following table

#  H1      Fist Class Honours                  70-100%
#  2.1     Second Class Honours, Grade 1       60-69%
#  2.2     Second Class Honours, Grade 2       50-59%
#  PS      Pass                                40-49%
#  FL      Fail                                0-39%


def level8_grade (mark: int) -> str:
    """
    Returns the level 8 grade for a given mark.
    
    :param mark: exam mark (0-100%)
    :return: grade description
    """
    if mark >= 70:
        return "H1 (Fist Class Honours)"
    elif mark >= 60:
        return "2.1 (Second Class Honours, Grade 1)"
    elif mark >= 50:
        return "2.2 (Second Class Honours, Grade 2)"
    elif mark >=40:
        return "PS (Pass)"
    else:
        return "FL (Fail)"
    
# if __name__ == "__main__":

#     print(level8_grade(40))
#     print(level8_grade(70))
#     print(level8_grade(50))

