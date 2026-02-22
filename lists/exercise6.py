# Exercise 6- Finding the longest Name
 # IT Technicians varying name lengths
# Determine the longest technician name , how many characters , display the result clearly


names = []
roles = []
years_experience = []


with open("staff.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, role, years = line.split(",")
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))


#assume first name is longest
longest_name = names[0]

#Compare with the rest
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

# Display result
print("Longest name: ", longest_name)
print("Number of characters: ", len(longest_name))
