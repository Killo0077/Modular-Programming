

def get_result(grade):
    if grade < 50:
        return "Fail"
    elif grade < 70:
        return "Pass"
    elif grade < 90:
        return "Merit"
    else:
        return "Distinction"


def main():
    names = ["Ana", "Luis", "Carlos", "Marta"]
    grades = [55,78,92,60]

    name = input ("Enter student name: ")
    grade = int(input(f"Enter grade for {name}: "))

    names.append(name)
    grades.append(grade)


    
# print(get_result(85))

    print("\nStudent Name       Grade       Result")
    print("----------------------------------")

    for i in range(len(names)):
        result = get_result(grades[i])
        print(f"{names[i]:20} {grades[i]:5} {result}")

if __name__ == "__main__":
    main()
