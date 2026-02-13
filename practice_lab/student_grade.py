


students = []
grades = []

count = int(input("How many students?: "))

for i in range(count):
    name = input("Student name: ")
    grade = int(input("Grade (0-100): "))

    students.append(name)
    grades.append(grade)

menu = """
1. Show all student
2. Show class average
3. Show highest grade
4. Show lowest grade
5. Find a student
6. Exit
"""

choice = int(input(menu))

while choice != 6:
    if choice == 1:
        print("\n---Student list----")
        for i in range(len(students)):
            print(students[i],"-",grades[i])

    elif choice == 2:
        if len(grades) >0:
            average = sum(grades) / len(grades)
            print("Class averages:", round(average,2))
        else:
            print("No student available")

        
    elif choice == 3:
        if len(grades) > 0:
            highest = max(grades)
            index = grades.index(highest)

            print("Highest grade: ")
            print(students[index], "-", highest)
        else:
            print("No students available.")
        
    elif choice == 4:
        if len(grades) >0:
            lowest = min(grades)
            index = grades.index(lowest)

            print("Lowest grade: ")
            print(students[index], "-", lowest)
        else:
            print("No students available")

    elif choice == 5:
        name = input("Enter student name: ")

        if name in students:
            index = students.index(name)
            print(name, "-", grades[index])        
        else:
            print("Invalid option")

    choice = int(input(menu))

print("Good bye")
