# Exercise — Student Result

# Write a function that determines if a student passed or failed.


def student_result (score1: int, score2: int, score3: int) -> str:
    """
    Determines if a student passed based on the average score.
    
    :param score1: first exam score
    :param score2: second exam score
    :param score3: third exam score
    :return: "Pass" or "Fail" 
    """
    average = (score1 + score2 + score3) / 3

    if average >= 50:
        return "Pass"
    else:
        return "Fail"
    

if __name__ == "__main__":

    print (student_result(60,55,70))    #True
    print (student_result(40,50,45))    #False