# Generate 50 numbers (1-3) and show frequencies.

import random

numbers = []

for i in range(50):
    numbers.append(random.randint(1,3))

for i in range(1,4):
    print(i,numbers.count(i))