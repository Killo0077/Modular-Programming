# (b) - Using a Python file as a module

# Create a new script file called using_circle.py.
# Import circle into this script, so that you can use its functions. It becomes a module.
# Add code that uses the circumference and area circle.
# !"If you are seeing more output than you expected, you may have forgotten the if
# statement that must be included in the module which says "Only if the run was started
# in this file should this file be run".


import circle

r = 5

print("Circumference: ", circle.circumference(r))
print("Area: ", circle.area(r))
