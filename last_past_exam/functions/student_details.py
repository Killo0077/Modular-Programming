

import random

def get_student_details():
    
    name = input("What is your name: ")
    
    while True:
        try:
            student_age = int(input("What is your age: "))
            if student_age > 0:
                break
            else:
                print("Age must be greater than 0")

        except:
            print("Please enter a valid number")

    return name, student_age



def generate_student_id(name, age):
    student_id = name[:2].upper() + str(age) + str(random.randint(1,9))
    return student_id




def main():
    name, age = get_student_details()
    student_id = generate_student_id(name, age)

    
    print("\n --- Student Details ---")
    print("name: ",name)
    print("Age: ", age)
    print("Student ID: ",student_id)

main()