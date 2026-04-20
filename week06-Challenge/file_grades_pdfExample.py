# Exam marks are stored in a file

#  This reads marks from a file and writes the corresponding grade into another file.


import grades

def get_file_name (prompt: str) -> str:
    """
    Ask the user for a file name.
    
    :param prompt: message to the user
    :return: file name
    """

    filename = input(prompt)
    return filename


if __name__ == "__main__":
    # Ask to input the file (mark file)
    input_file = get_file_name("Enter the input file name: ")
    output_file = get_file_name("Enter the ouput file name: ")

    # open the input file in read mode
    read_connection = open(input_file, "r")
    # file in write mode
    write_connection = open(output_file, "w")

    for line in read_connection:    # read (mark) from the input file
        mark = int(line.strip())    # Convert mark to int
        grade = grades.level8_grade(mark)

        print(f"{mark}% - {grade}", file= write_connection)

        #Close files
        read_connection.close()
        write_connection.close()
