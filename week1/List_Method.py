#### UNDERSTAND AND USING LIST METHODS

# Lists have inbuilt methods accessed using the dot operator e.g. numbers.count(4) counts the number of times 4 appears in the list called numbers.
# A function which is built into a list is called a method.

import random

numbers = []

n = int(input("Insert a number: \n"))

for i in range(n):
    numbers.append(random.randint(1, 20))
    print(i, numbers[i])

numbers.insert(3, random.randint(1, 20))
print(numbers)

print("5 appears", numbers.count(5), "times")


if 9 in numbers:
    print("9 is in Index", numbers.index(9))
else:
    print("9 is not in the Index")

count = 0
for i in range(len(numbers)):
    if numbers[i] >= 5:
        count += 1
        print(count)


for i in range(len(numbers)):
    numbers[i] += 11
    print(numbers)

for i in range(len(numbers)):
    print(i, numbers[i])
