# Book management system.


# Read from the list.

author = []
titles = []
years =[]
tags =[]

with open("records_book.txt","r") as file:
    for line in file:
        data = line.strip().split(",")

        author.append(data[0])
        titles.append(data[1])
        years.append(int(data[2]))
        tags.append(int(data[3]))

# print(f"{names},{titles},{years},{tags}")

# Menu processing

menu = """
1. Add a new book
2. Delete a book 
3. Update the sales figure of a book
4. Find books by an author
5. Find the oldest book(s)

"""

choice = int(input(menu))

while choice != 6:
    if choice == 1:
        print("Add a new book")
    elif choice == 2:
        print("Delete a book")
    elif choice == 3:
        print("Update the sales")
    elif choice == 4:
        print("Find by author ")
    elif choice == 5:
        print("Find the oldest book")

    choice = int(input(menu))
    print(menu)