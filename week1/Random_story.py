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

chosen_element = random.choice(characters)
chosen_action = random.choice(actions)
sentence.append(chosen_element)
sentence.append(chosen_action)
print(sentence)
