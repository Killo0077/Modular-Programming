# Book management system.


# Read from the list.

authors = []
titles = []
years =[]
tags =[]

with open("records_book.txt","r") as file:
    for line in file:
        data = line.strip().split(",")

        authors.append(data[0])
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
    # print(menu)



# Option 1 - Create

if choice == 1:
    print("Please, add a new book")
    title = input("Title:")

    if title in titles:
        print("That book is already in the list")
    else:
        author = input("Author: \n")
        year = int(input("Year: \n"))
        tag = int(input("Tag: \n"))

        titles.append(title)
        authors.append(author)
        years.append(year)
        tags.append(tag)

# Option 2 - Delete

elif choice == 2:
    print("What book would you delete: \n")
    title = input("Title to delete: ")

    if title in titles:
        index = titles.index(title)

        del titles[index]
        del authors[index]
        del years[index]
        del tags[index]
        print("Book deleted")
    else:
        print("Book not found!!!")



# Option 3 - Update

elif choice == 3:
    title = input("Title to update: \n")

    if title in titles:
        index = titles.index(title)
        print(f"{titles[index]} ({years[index]}) by {authors[index]} has sales of {tags[index]}")

        new_sales = int(input("New Sales: "))
        tags[index] = new_sales
    else:
        print("Book not found")