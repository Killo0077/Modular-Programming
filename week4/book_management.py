# Book management system.


names = []
titles = []
years =[]
tags =[]

with open("records_book.txt","r") as file:
    for line in file:
        data = line.strip().split(",")

        names.append(data[0])
        titles.append(data[1])
        years.append(int(data[2]))
        tags.append(int(data[3]))

print(f"{names},{titles},{years},{tags}")