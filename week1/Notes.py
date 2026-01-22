# First class


#### Lists ###

numbers = [5, 8, 6, 2, 7]

###### Tuples ########
numbers = (5, 8, 6, 2, 7)
# [index] - position - offset
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])

# numbers[0] = 7
# print(numbers[0])


beatles = ("John", "Paul", "George", "Ringo")
if "Cliona" in beatles:
    print("You share a name with a Beatle")


### List  -mutable - it can be changed

numbers = [5, 8, 6, 2, 7]
print(numbers)
numbers[0] += 7
print(numbers)


numbers = [5, 8, 2, 9]
print(numbers)
numbers2 = [4, 2, 6, 7, 4, 2]
new_list = numbers + numbers2
numbers.extend(numbers2)


numbers = [5, 8, 2, 9]
print(numbers)
numbers.append(3)
print(numbers)


numbers = [5, 8, 2, 9]
print(numbers)
numbers.insert(2, 11)  # (index:2  object:11)
print(numbers)


numbers = [5, 8, 2, 9]
x = numbers * 3
print(x)


count_letters = [0] * 26
print(count_letters)


numbers = [5, 8, 2, 9, 5, 7]
print(numbers)
numbers.remove(9)
print(numbers)
numbers.pop(1)
print(numbers)

# number_deleted = numbers.pop(1)

del numbers[3]
print(numbers)


numbers = [5, 8, 2, 9]
print(numbers)
print(numbers.count(7))
# print(numbers.index(88))  ## will crash becouse that numbers is not in the list
if 88 in numbers:
    print(numbers.index(88))
else:
    print("88 is not in the list")

# print(sum(numbers))
# print(max(numbers))
# print((numbers))
# print(sum(numbers))

numbers = [5, 8, 2, 9]
print(numbers)
# in place sorting
numbers.sort(reverse=True)
print(numbers)


##numbers sorted
numbers_sorted = sorted(numbers)
print(numbers)
print(numbers_sorted)


numbers = [5, 8, 2, 9]
copy = numbers.copy()
print(numbers, copy)
numbers[0] = 999
print(numbers, copy)


numbers = [5, 8, 2, 9]
print(numbers)
for i in range(10):
    print(i)


numbers = [5, 8, 2, 9]
numbers_of_numbers = len(numbers)
for i in range(numbers_of_numbers):
    # print(i)
    print(i, numbers[i])

for item in numbers:
    print(item)

for index in range(numbers_of_numbers):
    print(index, numbers[index])

for index, item in enumerate(numbers):
    print(index, item)
