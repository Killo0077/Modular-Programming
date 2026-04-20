# Create a list of 1000 random numbers between 1 and 10.
# Write code to count the number of 1's in the list, the number of 2's in the list etc. This can be done a variety of ways.

import random

numbers = []
for i in range(1000):
    numbers.append(random.randint(1,10))

counters = [0] * 10

for i in range(10):
    counters[i] = numbers.count(i + 1)

for i in range(10):
    print(i + 1, "appears", counters[i], "times")

max_count = max(counters)
most_common = counters.index(max_count) + 1     ##### Do it again


print("Most common number is:", most_common)
