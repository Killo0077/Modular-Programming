# Week 6 Challenge / Pairs



**Create a grades module**

**Use the module**
* Read the assessment mark
* Read the degree level
* Display the descriptive grade


**Exam marks are stored in a file **

Add a function to ask the user for the name of a file and return that file name.
Add code to:
1. Ask the user for a file's name (use the function)
2. Open a read connection to that file
3. Read each mark from the file as an integer
4. Print the grade (use level8_grade() from the grades module)


# Part 2 – write to a file

Reuse the function you have already written to ask the user for the name of a file and
returns that file name.
Add code to connect to this file in write-mode.
Add code to print each mark and grade to this file instead of to the screen.

# Part 3

The function above probably asks a generic question like "What is the name of the file?"
Adapt this function so that it receives the question (prompt) as a parameter.
For example, the following code uses the same function to get a file's name but the question
being asked is different each time – this is a much more useful function!

[alt text](../assets/week6-challenge.png)