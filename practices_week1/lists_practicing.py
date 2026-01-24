# Create a list with numbers from 1 to 10

numbers = []

for i in range(100):
    numbers.append(i+1)

print(numbers)

# Create a list 20 random numbers between 1 and 5

import random

numbers = []

for i in range(20):
    numbers.append(random.randint(1,5))

print(numbers)