# # Exercise — Student Grade

# # Write a function that returns the student's grade based on the average of 3 scores.

# | Average | Grade |
# | ------- | ----- |
# | 90+     | A     |
# | 80–89   | B     |
# | 70–79   | C     |
# | 60–69   | D     |
# | <60     | F     |


def student_grade(score1: int, score2: int, score3: int) -> str:
    """
    Calculate the student's grade based on the average score.
    
    :param score1: first exam score
    :param score2: second exam score
    :param score3: third exam score
    :return: grade (A,B,C,D,F)
    """

    average = (score1 + score2 + score3) / 3

    if average >= 90:
        return "A"
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
if __name__ == "__main__":

    print (student_grade(85,90,80)) # B
    print (student_grade(70,65,75)) # C 
    print (student_grade(40,50,30)) # F