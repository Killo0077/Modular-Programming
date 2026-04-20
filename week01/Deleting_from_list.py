######## DELETING FROM A LIST #######

# In each case print the list after you have edited it to verify the edit worked.

# remove(x) – removes the first occurrence of value x

# pop(i) – removes and returns the item at index i (last item if i is not given)

# clear() – removes all items from the list

# del – deletes an item (or slice(more next week)) by index

# Delete the number at index 1 from the list using .pop().
# Delete the number at index 2 using del().
# Use the in operator in an if statement to determine if there is a 19 in the list.
# If the number 19 is in the list, remove it using .remove(19).
# Remove all instances of the number 17 from the list using a while loop, the in operator as the condition and remove() as the method.


# Deleting using .pop
numbers = [33, 53, 1, 3, 98]
numbers.pop(1)
print(numbers)


# Deletes an item by index
del numbers[2]
print(numbers)

# Check if 19 is in the list, remove it using .remove(19)
if 19 in numbers:
    numbers.remove(19)
    print(numbers)

# Remove all instances of the number 17 using while loop

while 17 in numbers:
    numbers.remove(17)
    print(numbers)
