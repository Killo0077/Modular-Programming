#Create 2 lists: students and scores/ ask user to add 1 new student + score
# print all student with scores

class Student(): 
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("John",80)

print(s1.name, s1.score)
    

