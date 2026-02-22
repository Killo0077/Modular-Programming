# Exercise 8 - Counting Junior and Senior Technicians

# Junior: less than 3 years
# Mid-level: 3-6 years
# Senior: more than 6 years

names = []
roles = []
years_experience = []

with open("staff.txt", "r") as file:
    for line in file:

        line  = line.strip()

        if line == "":
            continue

        #split line and remove spaces
        name, role, years = [x.strip() for x in line.split(",")]

        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

# Counter
junior = 0
mid = 0
senior = 0

#check each technician
for years in years_experience:

    if years < 3:
        junior += 1
    elif years <= 6:
        mid +1
    else:
        senior += 1

# Display results
print("Junior technicians: ",junior)
print("Mid-level technicians: ",mid)
print("Senior technician: ", senior)

