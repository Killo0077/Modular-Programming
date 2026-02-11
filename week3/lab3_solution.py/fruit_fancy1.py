# Task 1 , Using same loop

fruits = []

with open("fruit.txt") as connection:
    for line in connection:
        fruits.append(line.strip().title())

print(fruits)
# sorts the words alphabetically in place (use .sort())
fruits.sort()
print(fruits)
# Writes the words in alphabetical order to a file called sorted1.txt
with open ("sorted.txt", "w") as output:
    for k in range(len(fruits)):
        print(fruits[k], file = output)

# Add code to print only those fruits that contain the letters 'an' are printed.
print()
print("Fruits with 'an': ")
for k in range(len(fruits)):
    if 'an' in fruits[k]:
        print(fruits[k])