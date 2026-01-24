# Generate 20 marks (0-100) and count how many passed (>40).

import random

marks = []

for i in range(20):
    marks.append(random.randint(0,100))

passed = 0

for mark in marks:
    if mark >= 40:
        passed += 1
    
print("Passed:",passed)