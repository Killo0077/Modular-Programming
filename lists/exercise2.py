#Exercise 2: Adding a New Technician

names =[]
roles =[]
years_experience =[]

with open("staff.txt","r") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        name,role,years = line.split(",")

        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

### Add a new technician
print("\nAdd new technician")

new_name = input("Enter name: ")
new_role = input("Enter role: ")
new_years =int(input("Enter years: "))

names.append(new_name)
roles.append(new_role)
years_experience.append(int(new_years))


print(f"{'No.':<4} {'Name':<25} {'Roles':<28} {'Years'}")
print("-" * 65)

for i in range(len(names)):
    print(f"{i+1:<4} {names[i]:<25} {roles[i]:<28} {years_experience[i]}")