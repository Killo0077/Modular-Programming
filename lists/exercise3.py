# Exercise 3: Deleting a Technician
# An IT Department needs to remove technicians who have left the company


names =[]
roles =[]
years_experience= []

with open("staff.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name,role,years = [x.strip() for x in line.split(",")]
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

#ask user for name to delete(case-sensitive)
search = input("Enter technician name to delete: ").strip().lower()

found_index = -1
                                                                        #### Better version ########
# Find the index
for i in range(len(names)):                                             # for i in range(len(names)):
    if names[i].lower() == search:                                      #       full_name = names[i].lower()
        found_index =1                                                  #       first_name = full_name.split()[0]
        break
                                                                        #       if search == full_name or search == first_name:
# If found -> remove from all lists and update file                     #           found_index = i
if found_index != -1:                                                   #           break
    names.pop(found_index)
    roles.pop(found_index)
    years_experience.pop(found_index)

    # Rewrite the file with update file
    with open("staff.txt","w") as file:
        for i in range(len(names)):
            file.write(f"{names[i]},{roles[i]},{years_experience[i]}\n")
    
    print("Technician removed and file updated.")

else:
    print("Error: Technician not found.")


