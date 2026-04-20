
## Task 1: Student Class & Lists
class Student:
    def __init__(self, name, student_id, course, year_of_birth):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.year_of_birth = year_of_birth

    def __str__(self): # Task 3 __str__  Note: Python prints a memory address if i don't define __str__
        return f"{self.name} ({self.student_id}) - {self.course} - {self.year_of_birth}"

    

# Task 2: Create the Main Function
def main():

    students = [
        Student("Sean Murphy", 1001, "Computing", 2006),
        Student("Aoife Byrne", 1002, "Business", 2007),
        Student("Cian O'Connor", 1003, "Engineering", 2005),
        Student("Niamh Kelly", 1004, "Computing", 2006), 
        Student("Darragh Walsh", 1005, "Science", 2006), 
        Student("Siobhán Doyle", 1006, "Business", 2007),
        Student("Tadhg Ryan", 1007, "Engineering", 2007), 
        Student("Orlaith McCarthy", 1008, "Science", 2002)
    ]

    for s in students:
        print(s)

# Task 4: Write a function that saves all student details to a .txt







if __name__ == "__main__":
    main()

