# Reading strings from file into list


# Create an empty list called fruits

fruits = []

# Open a connection to fruit.txt
# Read line by line through this file using for line in connection_name:
#   append the fruit to the fruits list, stripping the newline character, using fruit.append(line.strip())

with open("fruits.txt") as f:
    for line in f:
        fruits.append(line.strip())

# Print the fruits to the screen

print("The fruits are: ", fruits)

# Sorts the fruits alphabetically (use either fruits = sorted(fruits) or fruits.sort())

fruits.sort()

print(fruits)

# Writes the words in alphabetical order to a file called sorted.txt
    # open a 'w' connection to a file called sorted
    # go through the fruit one at a time e.g. for k in rage(len(fruits))  or for fruit in fruits:   or  for k, fruit in enumerate(fruits)

with open ("sorted.txt", 'w') as f:  ### Im using for fruit in fruits
    for fruit in fruits:
        f.write(fruit + "\n")

# Print only those fruits that contain the letters 'an'
    # go through the fruits one at a time
    # if 'an' in the fruit
    # print the fruit to the screen

for fruit in fruits:
    if 'an' in fruit:
        print(fruit)