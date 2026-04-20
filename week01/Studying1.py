###### WEEK 1 - LECTURE

# Creating a list

fruits= ['mango','banana','pinapple']
print(fruits)

# Common Operations on list /// Accessing Elements:
print(fruits[0]) #Output: 'mango'
print(fruits[1]) #Output: 'banana'
print(fruits[2]) #Output: 'pinapple' 
#print(fruits[3]) #Output: exception - IndexError: list out of range

# Navigate Indexing
print(fruits[-1]) #Output: 'pinapple'
print(fruits[-2]) #Output: 'banana'
print(fruits[-3]) #Output: 'mango' 
#print(fruits[-4]) #Output: exception - IndexError: list out of range


##### Modifying Elements:
fruits[1]= 'blueberry'
print(fruits) # Output: ['mango','blueberry','pinapple']


##### Adding Elements to the List #######

fruits.append('date')  # add to the end of the list
fruits.insert(1, 'banana') # insert at index 1 of the list

print(fruits) # Output: ['mango','banana','blueberry','pinapple','date']


##### List extend()
# list1.extend(list2) - adds all the elements of list2 on to the end of list. Where append() adds a single element at the end of the list, extend() 
# adds a single element at the end of the list, extend() adds another list to the end of the list

list1 = [1,2,3]
list2 = [4,5]
list1.extend(list2) # extend= add all list2 items to list1
print(list1) #Output: [1,2,3,4,5]


##### List +
# The + operator is similar to extend() function: + adds two lists to make a new bigger list.
# The += operator may be used like extend()
fruits = ['mango','banana','pineapple']
more_fruits= ['lemon','grape']
new_list = fruits + more_fruits     #Make new combined list
fruits += ['plum','orange'] # += modifies fruits like extend()

###### List += Error
# Sometimes a programmer will mistakenly write += to add a single element to a list. This does not work, since List + and += only
# add a lists of elements, not a single element. The run-time error here refers to an object not being iterable which means it cannot 
# return each contained value one at a time because it has only 1 value.
1st = [1,2,3]
fruits += 'grapefruit'

TypeError: 'int' object is not iterable

# Use append() to add a single element.
1st =[1,2,3]
1st.append('grapefruit')


###### Removing Elements:
# remove(x) - removes the first occurrence of value x
# pop(i) - removes and returns the item at index i (last item if i is not given)
# clear() - removes all items from the list
# del - deletes an item (or slice) by index 
fruits = ['mango','banana','blueberry','pineapple','date']
fruits.remove('banana')
print(fruits) # Output : ['mango', 'blueberry', 'pineapple', 'date']

fruits.remove('orange') # Output: ValueError: list.remove('orange'): 'orange' not in list

fruits.pop(2)
print(fruits)  # Output: ['mango', 'blueberry', 'date']

fruits.pop(88) # Output: IndexError: pop index out of range


##### Using sort():
# This method sorts the list in place, meaning the original list is changed. You can sort numbers or strings
# in ascending order by default.
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]
numbers.sort(reverse = True)
print(numbers) # Output: [9, 5, 2, 1]


##### Using count():
#This method returns the number of times a specific value appears in the list
fruits = ['apple', 'banana', 'apple', 'cherry']
print(fruits.count('apple'))  # Output: 2

###############################################################################################
##### Using index() with Exception Handling:
# This method returns the index of the first occurrence of a value in the list. If the value is not present, it raises a ValueError.
# You can use the in operator to check first and avoid the exception.
fruits = ['apple', 'banana', 'cherry']

# Using in operator to avoid exception
if 'banana' in fruits:
    print(fruits.index('banana'))  # Output: 1

# Example that could raise an exception and how to handle it
try:
    print(fruits.index('orange'))  # 'orange' is not in the list
except ValueError:
    print("'orange' is not in the list!")  # Output: 'orange' is not in the list!

################################################################################################


#### Python'a Build-in Functions for list
# len(): Returns the number of items in the list.
# sorted(): Returns a sorted list without changing the original list. To change the list 'in-place' use the list method .sort().
# sum(): Returns the sum of all elements (works with numerical lists).
# max() / min(): Returns the maximum or minimum value.

numbers = [3, 1, 4, 1, 5, 9]
print(len(numbers))      # Output: 6
print(sorted(numbers))   # Output: [1, 1, 3, 4, 5, 9]
print(sum(numbers))      # Output: 23
print(max(numbers))      # Output: 9
print(min(numbers))      # Output: 1


######## Iterating Through Lists
# There are multiple ways to iterate through lists in Python:

#### Using range() and leng() with []:
for i in range(len(fruits)):
    print(fruits[i])  # Output: each fruit on a new line

#### Using a for item in list:
# If you do not wish to edit the list and therefore do not have to use [] choose this loop.

for fruit in fruits:
    print(fruit)  # Output: each fruit on a new line

### Using enumerate():
#This provides the value and its index at each iteration, so that you can print where it is and what it is. 
#(It also has other uses but this suffices for now.)

for index, fruit in enumerate(fruits):
    print(index, fruit)  # Output: index and fruit on a new line