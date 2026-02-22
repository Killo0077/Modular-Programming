# Exercise 5- Average years of experience

names = []
roles =[]
years_experience = []


#read file
with open("staff.txt","r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, role, years = line.split(",")
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))


# Calculate average
average = sum(years_experience) / len(years_experience)

#find highest
highest = max(years_experience)

#find lowests
lowest = min(years_experience)

#Display results
print("Average years: ", round(average, 2))
print("Highest years: ", highest)
print("Lowest years: ", lowest)