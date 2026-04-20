# Week 3 - Lab  SOLUTIONs
# Task 1 reading strings from file

fruits = []

with open ("fruit.txt") as connection:
    for line in connection:
        fruits.append(line.strip().title())

# sorts the words alphabetically in-place (use .sort())
fruits.sort()

# write the words in alphabetical order to a file called sorted.txt
with open("sorted.txt", "w") as output:
    print("\n".join(fruits), file=output)

# Add code to print only those fruits that contain the letters 'an' are printed.
fruits_with_an = [fruit for fruit in fruits if "an" in fruit]
string = "and ".join(fruits_with_an)
print(" 'an' is in", string)

#In one line
print("'an' is in ", " and ".join([fruit for fruit in fruits if "an" in fruit]))

