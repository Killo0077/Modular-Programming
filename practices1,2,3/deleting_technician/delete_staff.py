# Delete Technician Program

names = []
roles =[]
years_experience = []

# Rear original file
with open("../staff_records/staff.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, role, years = [x.strip() for x in line.split(",")]
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

# Ask user for name to delete
search = input("Enter technician name to delete: ").strip().lower()

found_index = -1

for i, name in enumerate(names):
    if name.lower() == search:
        found_index = i 
        break

# If found --> remove from list
if found_index != -1:
    names.pop(found_index)
    roles.pop(found_index)
    years_experience.pop(found_index)

    print("Technician removed successfully. ")

# Save to new file (safe copy)
    with open("../staff_records/staff_updated.txt", "w") as file:
        for name,role, year in zip(names, roles, years_experience):
            file.write(f"{name}, {role}, {year}\n")
    
    print("Updated list saved to starff_updated.txt")

else:
    print("Technician not found.")
