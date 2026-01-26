############## ** PYTHON LISTS ** ############

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



