# Exercise 9: Report Generation

names = []
roles = []
years_experience = []

with open("staff.txt", "r") as file:
    for line in file:

        line = line.strip()

        if line == "":
            continue
        
        #split and clean spaces
        name, role, years = [x.strip() for x in line.split(",")]

        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

#total technicians
total = len(names)

#average experience
average = sum(years_experience) / total

# longest name
longest_name = name[0]
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

# count categories
junior = 0 
mid = 0
senior = 0

for years in years_experience:
    if years < 3:
        junior += 1
    elif years <= 6:
        mid +=1
    else: 
        senior +=1

# report file
with open ("report.txt", "w") as file:

    file.write("IT Staff Report\n")
    file.write("------------------------\n")
    file.write("Total technicians: {total}\n")
    file.write(f"Average experience: {round(average,2)} years\n")
    file.write(f"Longes name: {longest_name}\n")
    file.write(f"Junior Technicians: {junior}\n")
    file.write(f"Mid-level technicians: {mid}\n")
    file.write(f"Senior technicians: {senior}\n")

print("Report created successfully.")