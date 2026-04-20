# Use the following code to create a list of 30 random numbers between 1 and 40 using list comprehension:


import random

numbers = [random.randint (1,40) for count in range (30)]

print(numbers)


#########################  list[start : end : step] !!!!!!!!!!!

#1. Use slicing to create and print lists made up of:
#----------------------------------------------------#

# 1. First 10 values

print(numbers[:10])

#2. Last 7 values
print(numbers[-7:])

#3. Every second value
print(numbers[::2])

#2. Use list comprehension to create and print lists made up of:
#--------------------------------------------------------------#

# 1. The odd values from numbers (requires an if statement in the list comprehension)

odds= [n for n in numbers if n % 2 !=0]
print(odds)

# 2. The above-average values (  you must calculate average and use that in the if statement of the list comprehension statement)

avg = sum(numbers) / len(numbers)
above_avg = [n for n in numbers if n > avg]
print(above_avg)


#3. Calculate and print the sum of the first 20 values using sum() on a 'sliced' list.
#------------------------------------------------------------------------------------#

print(sum(numbers[:20]))

#4. Calculate and print the sum of the values between indices 10 and 19 inclusive. Do this two ways to verify your answers.
#-------------------------------------------------------------------------------------------------------------------------#
print(sum(numbers[10:20]))

#5. Count and print the number of values that are less than 10. Do this two ways to verify your answer.
#-----------------------------------------------------------------------------------------------------#

