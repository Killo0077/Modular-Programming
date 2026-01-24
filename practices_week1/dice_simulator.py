# Roll a dice 30 times and count results.

import random

rolls = []

for i in range(10):
    rolls.append(random.randint(1,6))

print("Times    Number")
 

for i in range(1,7):
    print(i,"       ",rolls.count(i))