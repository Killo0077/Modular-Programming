# # Exam marks are stored in a file.

# Add a function to ask the user for the name of a file and return that file name.
# Add code to:
# 1. Ask the user for a file's name (use the function)
# 2. Open a read connection to that file
# 3. Read each mark from the file as an integer
# 4. Print the grade (use level8_grade() from the grades module)

import grades

def get_file_name(prompt: str) -> str:
    """
    Ask the user for the file name.

    :param promt: message displayed to the user
    :return: file name
    """

    filename = input ("Enter the file name: ")
    return filename

if __name__ == "__main__":
    # filename = get_file_name()            #part 1
    input_file = get_file_name("What is the name of the input file? ")
    output_file = get_file_name("What is the name of the file to store the results? ")

    # with open(filename, "r") as file:     # part 1
    with open (input_file, "r") as read_file, open(output_file, "w") as write_file:
            for line in read_file:
        # for line in file:     # part 1    
                mark = int(line.strip())
                grade = grades.level8_grade(mark) 

                print(f"{mark}% - {grade}", file = write_file)
       
    # read_connection = open(filename, "r")         # part 1
                                                    # <<<<-- pdf example 
    # for line in read_connection:
    #     mark = int(line)
    #     grade = grades. level8_grade(mark)

    #     print(f"{mark}% - {grade}")

    # read_connection.close()