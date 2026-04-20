#### Undertanding sorted() versus list method sort() #######

# .sort() modifies a list in place and returns nothing, while sorted() returns a new sorted list.

# Make and print a sorted copy of the list using Python's built-in function, sorted().
# Sort the list in-place using .sort(), and print the newly sorted list.

numbers = [2, 5, 11, 9, 3]
print(numbers)

numbers_sorted = sorted(numbers)
print(numbers_sorted)


numbers = [12, 3, 55, 2]

numbers.sort()
print(numbers)


###### sorted(list) ---> new list
###### list.sort() ----> changes list
