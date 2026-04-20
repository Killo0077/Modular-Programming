

scores = [9,8,6,7,6]
judges = ["Kim","Tim","Finn","Lynn","Wynn"]

#1. Ask for a judge's name and their score and append these to the list.
judge = input("Enter judge name: ")
score = int(input("Enter score: "))

judges.append(judge)
scores.append(score)

print(judge)
print(score)

#2. Print the data as a neat table using zip()
print("-----------------")
print("Score      Judges")
print("-----------------")

for score, judge in zip(scores, judges):
    print(score,"          ",judge)

print("-----------------\n\n")

#3. Print the data as a neat table without using zip() - for index, value in enumerate(score) or for index in range(len(scores))
print("-----------------")
print("Score      Judges")
print("-----------------")

for i in range(len(scores)):
    print(scores[i] ,"         ", judges[i],"\n")
    

#4. Calculate and print the average score

avg = sum(scores) / len(scores)
above_avg = [n for n in scores if n > avg]
print(above_avg, "\n")

#5. Use the min() and max() functinos to print the highest and lowest scores.
lowest = min(scores)
highest = max(scores)
print("====================")
print(f"Lower scores {lowest}")
print(f"Highest scores {highest}")
print("====================","\n\n")

#6. Print the name(s) of those judge(s) who awarded the lowest score
judges = ["Kim", "Tim", "Finn", "Lynn", "Wynn"]
scores = [9, 8, 6, 7, 6]

lowest = min(scores)

print("Judge(s) with the lowest score:")
for i in range(len(scores)):
    if scores[i] == lowest:
        print(judges[i],"\n")

#7. Count and print the number of judges who gave a score of 7 or above.

greater_7 = len([score for score in scores if score >= 7]) #### check
       
print(greater_7)


############# different way/
greater_7 = 0
for i in range (len(scores)):
    if scores[i] >=7:
        greater_7 += 1
print (greater_7)  ## !!!!!


greater_7 = 0
for score in scores: 
    if score >=7:
        greater_7 += 1
print(greater_7)



