############## ** PYTHON LISTS ** ############


List slicing is a powerful feature in Python that allows you to extract specific parts of a list.

It uses the syntax 'list[start:stop:step]', where 'start' is the index where the slice begins, 'stop' is the index where the slice ends (exclusive), and 'step' is the interval between elements.

For example, 'list[1:5:2]' would give you every second element from index 1 to 4.

By omitting 'start', slicing starts from the beginning of the list.
By omitting 'stop', slicing goes until the end of the list.
By omitting 'step', slicing uses the default step of 1.
List comprehensions are a concise way to create lists in Python. They allow for the generation of a new list by applying an expression to each item in an existing iterable, such as a list or range, and optionally filtering items based on a condition. The syntax is [expression for item in iterable if condition]. For example, [x**2 for x in range(10) if x % 2 == 0] creates a list of the squares of even numbers from 0 to 9. List comprehensions are more readable and more efficient than using traditional loops for creating lists.




1. # List Slicing 
    - Syntax : list[start:stop:step]
    - start default = 0, stop= end, default = 1
    - Stop index is exclusive
    - Example:
        * [:5] from start to index 4
        * [2:] index 2 to end
        * [0:7:2] every second element


2. # List Comprehensions
    - Short, efficient way to create lists
    - Syntax: 
        [expression for item in iterable if condition]
    - Faster and cleaner than `for + append`
    
    - Example:
        `[i * 10 for i in range(20)]`
      
    - _ is used when loop variable isn't important


3. # Strings as Sequences
    - Strings behave like lists ( can slice, iterate, use `in`)
    - Strings are immutable --> cannot change characters directly
    

4. # String Methods
    - Common methods:
        * count()       count occurrences
        * index()       position (error if not found)
        * find()        positon or -1
        * replace()     returns new string
        * split()       string --> list
        * join()        list --> string

5. # Parallel List
    - Multiple lists where indexes are related
    - Example:
        `students = ["Alice", "Bob"]`
        `grades = [85, 90]`

    - Cleanest way to handle parallel lists


7. # User Input & Lists
    - Start with empty list[]
    - Use `.append()` to add data
    - `_` used when loop counter isn't needed


////////////////////////////////////////////////////////////////////////////////////////////////////////

# ################### QUICK REVIEW #########################

# List 
* Mutable (can change)
* Index starts at 0
* Methods: append() , count() , index()

# Slicing
a[start:stop:step]

    - Stop is exluded
    - [: ] --> copy
    - [::2] --> every second item

# List Comprehension
[new_value `for` item `in` iterable `if` condition]

    - Faster + cleaner than loops
    - Use `_` if variable not used

# Strings
* Sequences (slice, loop, in)
* Immutable
* Common methods:
    count(), find(), replace(), split(), join()

# Parallel List
* Same Index = related data
* Best way to loop: `zip()`



