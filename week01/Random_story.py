##### RANDOM STORY BUILDER #########

# Write a program that constructs the first sentence of a story.
# The story should follow this format: character action object place
# Example Sentence:
# "A knight discovered a hidden treasure in the forest."


import random

characters = ["a wizard", "a knight", "a dragon", "a princess", "a unicorn"]
actions = ["found", "lost", "fought", "discovered", "stole"]
objects = [
    "a magical wand",
    "a golden shield",
    "a hidden treasure",
    "an ancient book",
    "a mysterious potion",
]
places = [
    "in the forest",
    "at the castle",
    "on the mountain",
    "in the village",
    "by the river",
]

sentence = []

chosen_character = random.choice(characters)
chosen_action = random.choice(actions)
chosen_object = random.choice(objects)
chosen_place = random.choice(places)

sentence.append(chosen_character)
sentence.append(chosen_action)
sentence.append(chosen_object)
sentence.append(chosen_place)

sentence[0] = sentence[0].capitalize()

for word in sentence:
    print(word, end=" ")
print()   # new line

#################################################################################################

#  COUNTING NUMBERS
# Create a list of 1000 random numbers between 1 and 10.
# Write code to count the number of 1's in the list, the number of 2's in the list etc. This can be done a variety of ways.

import random

numbers= []

for i in range(1000):
    numbers.append(random.randint(1,10))

counters = [0] * 10

for value in range(1,11):
    counters[value -1] = numbers.count(value)

print("Numbers      Occurrences")
print("========================")

for i in range(10):
    print(i + 1,"   ",counters[i])


######################################################################################

#  MOST COMMON NUMBER
# Add code to display the most common number in the list of random numbers. You may assume the largest count is unique. 
# This can be done without loops using max() to find the largest number and .index() 
# to find its index. Knowing its index is a simple +1 to get the number. 

for num in numbers:
    counters[num -1] += 1
