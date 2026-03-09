# # Exam marks are stored in a file.

# Add a function to ask the user for the name of a file and return that file name.
# Add code to:
# 1. Ask the user for a file's name (use the function)
# 2. Open a read connection to that file
# 3. Read each mark from the file as an integer
# 4. Print the grade (use level8_grade() from the grades module)

import grades

def get_file_name() -> str:
    """
    Ask the user for the file name.
    :return: file name
    """

    filename = input ("Enter the file name: ")
    return filename

if __name__ == "__main__":
    filename = get_file_name()

    with open(filename, "r") as file:

        for line in file:
            mark = int(line.strip())
            grade = grades.level8_grade(mark) 

            print(f"{mark}% - {grade}")
       
    # read_connection = open(filename, "r")
                                                    # <<<<-- pdf example 
    # for line in read_connection:
    #     mark = int(line)
    #     grade = grades. level8_grade(mark)

    #     print(f"{mark}% - {grade}")

    # read_connection.close()