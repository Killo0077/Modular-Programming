

student_ids = [1,2,3,4,6]
scores = [45,70,82,30,90]

print("ID   Score   Grade")
print("-"* 26)

for i in range(len(student_ids)):

    score = scores[i]

    if score < 50:
        grade = "Fail"
    elif score <= 79 :
        grade = "Pass"
    else:
        grade = "Distinction"

    print(f"{student_ids[i]:<5}{score:<8}{grade}")




