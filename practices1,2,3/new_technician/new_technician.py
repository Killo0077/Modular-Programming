# IT Technicians hired

names = []
roles = []
years_experience = []

# Read existing staff list

with open("staff.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, role, years = [x.strip() for x in line.split(",")]
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

# Ask for new technician
print("\n----- Add a New Technician -----")

new_name = input("Enter technician name: ").strip()
new_role = input("Enter job role: ").strip()
new_years = int(input("Enter year of experience: "))

names.append(new_name)
roles.append(new_role)
years_experience.append(new_years)

# Write new Technician to file

with open("staff.txt", "w") as file:
    for name, role, year in zip(names, roles, years_experience):
        file.write(f"{name},{role},{year}\n")

print("Technician added successfully!")
