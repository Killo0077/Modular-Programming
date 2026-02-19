# Exercise 1: Reading Staff Records

# Create an empty  lists to store the data
names =[]
roles = []
years_experience = []

# Open the file for reading
with open("staff.txt","r") as file:
    for line in file:
        line = line.strip() # remove newline and spaces.!!!

        if line =="":
            continue

        name,role,years = line.split(",") # split the line into 3 parts

        names.append(name)
        roles.append(role)
        years_experience.append(int(years))

print(f"{'No.':<4} {'Name':<25} {'Roles':<28} {'Years' }")
print("-" * 65)

# loop through lists together
for i in range(len(names)):
    print(f"{i+1:<4} {names[i]:<25} {roles[i]:<38} {years_experience[i]}")

print("\nTotal technicians:", len(names))