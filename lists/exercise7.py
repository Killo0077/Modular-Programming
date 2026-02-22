# Exercise 7 - Filter by Role


names = []
roles = []
years_experience = []

with open("staff.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, role, years = [x.strip() for x in line.split(",")] ###!!! split line into parts and remove extra spaces, cleans spacess 
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))


search_role = input("Enter job role: ").strip().lower()

found = False

#check each technician
for i in range(len(names)):
    if roles[i].lower() == search_role:
        print(names[i], "|", roles[i], "|", years_experience[i])
        found = True

# if nothing found
if found == False:
    print("No technician found with that role.")

