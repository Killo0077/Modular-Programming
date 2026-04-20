#### WEEK 1 - LAB #########


# Basics of list including Looping through List
# a
numbers = [3, 5, 8, 1]
print(numbers)

# b
numbers = [3, 5, 8, 1]
print(numbers[0])

# c
numbers = [3, 5, 8, 1]
print(numbers[-1])

# d
numbers = [3, 5, 8, 1]
print(numbers[1])

# e
numbers = [3, 5, 8, 1]
print(numbers[-2])

# f
numbers = [3, 5, 8, 1]
print(len(numbers))

# g
numbers = [3, 5, 8, 1]
print(sum(numbers))

# h
numbers = [3, 5, 8, 1]
average = sum(numbers) / len(numbers)
print(average)

# i
numbers = [3, 5, 8, 1]
for item in numbers:
    print(item)

# j
numbers = [3, 5, 8, 1]
for i in range(len(numbers)):
    print(i)

# k
numbers = [3, 5, 8, 1]
for i, item in enumerate(numbers):
    print(i, item)


# l
numbers_copy = numbers.copy()

# m
numbers = [3, 5, 8, 1]
numbers_copy = numbers.copy()

for i, item in enumerate(numbers_copy):
    numbers_copy[i] = item + 1

print(numbers_copy)

# n
for i, item in enumerate(numbers_copy):
    numbers_copy[i] = item + 1
