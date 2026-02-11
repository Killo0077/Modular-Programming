# Book management system.


# Read from the list.

authors = []
titles = []
years =[]
sales =[]

with open("records_book.txt","r") as file:
    for line in file:
        data = line.strip().split(",")

        authors.append(data[0])
        titles.append(data[1])
        years.append(int(data[2]))
        sales.append(int(data[3]))

# print(f"{names},{titles},{years},{tags}")

# Menu processing

menu = """
1. Add a new book
2. Delete a book 
3. Update the sales figure of a book
4. Find books by an author
5. Find the oldest book(s)
6. Quit

"""

choice = int(input(menu))

while choice != 6:


    # if choice == 1:
    #     print("Add a new book")
    # elif choice == 2:
    #     print("Delete a book")
    # elif choice == 3:
    #     print("Update the sales")
    # elif choice == 4:
    #     print("Find by author ")
    # elif choice == 5:
    #     print("Find the oldest book")

    # choice = int(input(menu))
    # print(menu)



# Option 1 - Create

    if choice == 1:
        print("======================")
        print("Please, add a new book: \n")
        title = input("Title:")

        if title in titles:
            print("That book is already in the list")
        else:
            author = input("Author: \n")
            year = int(input("Year: \n"))
            sale = int(input("Sale: \n"))

            titles.append(title)
            authors.append(author)
            years.append(year)
            sales.append(sale)

# Option 2 - Delete

    elif choice == 2:
        print("==============================")
        print("What book would you delete: \n")
        title = input("Title to delete: ")

        if title in titles:
            index = titles.index(title)

            del titles[index]
            del authors[index]
            del years[index]
            del sales[index]
            print("Book deleted")
        else:
            print("Book not found!!!")



# Option 3 - Update

    elif choice == 3:
        title = input("Title to update: \n ==> ")
        

        if title in titles:
            index = titles.index(title)
            print(f"{titles[index]} ({years[index]}) by {authors[index]} has sales of {sales[index]}")

            new_sales = int(input("New Sales: "))
            sales[index] = new_sales
        else:
            print("Book not found")

    # print(menu)

# Option 4 - Books by an author

    elif choice == 4:
        name = input("\nAuthor name: \n ==> ")
        found = [titles[i] for i in range(len(authors)) if authors[i] == name]

        if found:
            print(",".join(found))
        else:
            print("**************")
            print("Sorry, No books found")
            print("**************")

# Option 5 - Oldest book(s)

    elif choice == 5:
        oldest_year = min(years)

        for i in range(len(years)):
            if years[i] == oldest_year:
                print("===============================================")
                print("  *** ",authors[i], "-", titles[i], " ***",)
                print("===============================================")
    choice = int(input(menu)) 
    
    


# Option 6 - Quit

with open("records_book.txt","w") as file:
    for author, title, year, sale in zip (authors, titles, years, sales):
        file.write(f"{author},{title},{year},{sale}\n")

print("Thank you, GoodBye!!!")