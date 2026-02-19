# Exercise 4: Editing Technician Details

# IT Techniciand may change roles or gain experience over time.


names = []
roles =[]
years_experience =[]

# Read file
with open("staff.txt","r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, role, years = [x.strip() for x in line.split(",")]
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

# Ask user for technician name.
search = input("Enter technician name to edit: ").strip().lower()

found_index = -1

# Find the technician (match full name OR first name)
for i in range(len(names)):
    full_name = names[i].lower()
    first_name= full_name.split()[0]    # [0] first item in the array

    if search == full_name or search == first_name:
        found_index = i
        break

# If found, ask what to update
if found_index != -1:
    print("\nFound:", names[found_index], "|", roles[found_index],"|",years_experience[found_index])

    print("\nWhat do you want to update?")
    print("1`.Job role")
    print("2.Years experience")

    choice = int(input("Enter 1 or 2:").strip())

    if choice == 1:
        new_role = input("Enter new role: ").strip()
        roles[found_index]= new_role
    
    elif choice == 2:
        new_years = int(input("Enter new years of experience: "))
        years_experience[found_index] = new_years
    
    else:
        print("Invalid choice. Nothing updated.")

# Save updated data back to file
    with open("staff.txt","w") as file:
        for i in range(len(names)):
            file.write(f"{names[i]}, {roles[i]}, {years_experience[i]}\n")

# Display updated record
    print("\nUpdated record: ")
    print(names[found_index], "|",  roles[found_index],"|",years_experience[found_index])

else:
    print("Error: Technician not found.")
