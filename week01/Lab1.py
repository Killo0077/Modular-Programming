# Basics of list including Looping Through List

#a. Create a list called numbers containing 4 numbers: numbers= [6,5,8,7]
numbers= [6,5,8,7]

#b. Print the last number in the list using [0]
print(numbers[3])

#c. Print the last number in the list using [-1]
print(numbers[-1])

#d. Print the second number in the list
print(numbers[1])

#e. Print the second last number in the list
print(numbers[-2])

#f. Print the lengh of the list using len()
print(len(numbers))

#g. Print the sum of the numbers in the list using sum()
print(sum(numbers))

#h. Calculate and print the average of the numbers in the list using(f) and (g)
print(sum(numbers)/ len(numbers))

#i. Use a loop to print each item in numbers (for item in numbers)
for item in numbers:
    print(item)

#j. Use a loop to print each item in numbers along with their index (for i in range(len(numbers)))
for i in range(len(numbers)):
    print(i,numbers[i])

#k. Use a loop to print each item in numbers along with their index using enumerate() (for i, item in enumerate(numbers))
for i, item in enumerate(numbers):
    print(i,item)

#l. Make a copy of numbers using the copy() method.
numbers_copy = numbers.copy()

print()

#m. Add 1 to each item in the copy using either the loop construct from (j) or (k) but not (i).
for i in range(len(numbers)):
    numbers_copy[i] += 1

for i in range(len(numbers)):
    print(numbers[i],numbers_copy[i])

print()    

#n. Print the original and modified lists side by side using the loop construct form (j)
for i in range(len(numbers)):
    print(numbers[i], numbers_copy[i])

###########################################################################################################
#################################################################################
#################################################
# UNDERSTAND AND USING LIST METHOD

#1. Create an empty list using numbers = []
import random

#2.Ask the user for a number. Write a loop that iterates that many times.
n= int(input("How many random numbers?"))

#3.On each iteration generate a random number between 1 and 20.
for i in range(n):
    r= random.randint(1,20)
    numbers.append(r)

#4. Print the list as a neat table using loop.
print("Index Value")

for i in range(len(numbers)):
    print(i,"    ",numbers[i])

#5. Generate a new random number and insert it at index 3 in the list using .insert(). Print the list using print(numbers)
new_number= random.randint(1,20)
numbers.insert(3, new_number)

print(numbers)

#6. Count and print the number of times 5 appears in the list using .count().
count_5 = numbers.count(5)
print(count_5)

#7. Use the in operator to check if 9 is in the list. If 9 is in the list, use the index(x) method to determine where it is.
if 9 in numbers:
    print("9 is in the list at index",numbers.index(9))
else:
    print("9 is not in the list")

#8. Count the numbers greater than or equal to 5 using a loop.
count_greater_5 = 0

for item in numbers:
    if item >= 5:
        count_greater_5 +=1
print(count_greater_5)

#9. Use a loop to increase each value in numbers by 11 using numbers[index] += 11
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 11
print(numbers)

#10. Print the index and the values next to each other in a neat table.
print("Index    Values")

for i in range(len(numbers)):
    print(i, "      ",numbers[i])
##########################################################################################
##############################################################################
############################################################

#Undertanding sorted() versus list method sort()
# .sort() modifies a list in place and returns nothing, while sorted() returns a new sorted list.
#1. Make and print a sorted copy of the list using Python's built-in function, sorted().
sorted_numbers = sorted (numbers)

print("Original list", numbers)
print("Sorted copy: ", sorted_numbers)

#2. Sort the list in-place using .sort(), and print the newly sorted list.
numbers.sort()

print("After sort(): ",numbers)

##################################################################################
#####################################################################
########################################################

#1. Delete the number at index 1 from the list using .pop()
numbers.pop(1)
print(numbers)

#2. Delete the number at index 2 using del()
del numbers[2]
print(numbers)

#3. Use the in operator in an if statement to determine if there is a 19 in the list. If the number 19 is in the list, remove it using .remove(19)
if 19 in numbers:
    numbers.remove(19)

print(numbers)

#4. Remove all instances of the number 17 from the list using a while loop, the in operator as the condition and remove() as the method.
while 17 in numbers:
    numbers.remove(17)

print(numbers)

####################################################################################################
##############################################################################
##############################################################
# List of Strings
# Copy the following code to create a list called countries
countries = ["spain","brazil","portugal","bolivia", "ireland", "italy"]

#1. Print the countries using print()
print(countries)

#2. Use a loop to edit the list so that each country is in a proper case i.e. Spain not spain, using title()
for i in range(len(countries)):
    countries[i] = countries[i].title()

#3. Print the countries using print()
print(countries)

#4. Append "Australia" to the end of the list.Print
countries.append("Australia")
print(countries)

#5. Insert "Iceland" at index 2. Print
countries.insert(2,"Iceland")
print(countries)

#6. Remove "Bolivia" from the list. Print
countries.remove("Bolivia")
print(countries)

#7. Ask the user for the name of a country. As long as the given country is in the list (use in operator in the condition of a while loop)
# ask them again, until they provide a country which is not in the list, then append it to the list. A sample run of this snippet might be:
# Country to add? Spain
# Country to add? Brazil
# Country to add? Germany
# ['Spain', 'Iceland', 'Brazil', 'Portugal', 'Ireland', 'Italy', 'Australia', 'Germany']

new_country = input("Country to add??:").title()

while new_country in countries:
    new_country = input("Country to add??: ").title()

countries.append(new_country)
print(countries)

##########################################################################
##############################################################
################################################
# Add a loop to count the countries that begin with "I'. This requires a new counting variable initialised to 0 which will be
#  incremented each time a country beginning with 'I' is found in the list.
#  (You may know about comprehension lists but don't use them for now).
count_i = 0

for country in countries:
    if country.startswith("I"):
        count_i += 1

print(count_i)
