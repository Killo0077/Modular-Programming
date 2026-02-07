# Read the file into three parallel lists:

names = []
roles = []
years_experience = []

# Read file into 3 parallels list

with open("staff.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, role, years = line.split(",")
        names.append(name)
        roles.append(role)
        years_experience.append(int(years))


# Display formatted table
print(f"{'No.':<4} {'Name':<25} {'Role': <28} {'Years':<5}")
print("=" * 70)

for i, (name, role, years) in enumerate(zip(names, roles, years_experience), start=1):
    print(f"{i:<4} {name :<25} {role :<28} {years :<5}")

# Total number of technicians
print("\nTotal technicians:", len(names))


######################## extra #################

# Average years of experience

average = sum(years_experience) / len(years_experience)
print(
    "\nAverage years:", round(average, 2)
)  # Use round,2 to round the number to 2 decimal places.


# Find a staff member

search = input("\nEnter a name: ").strip().lower()

for name, role, year in zip(names, roles, years_experience):
    full = name.strip().lower()
    first = full.split()[0]  # first word

    if search == full or search == first:
        print("*" * 48)
        print(f"\nFound: {name } | {role} | {year}")
        print("*" * 48)
        break
else:
    print("\nNot found")


# Sho only staff with +5 years

for name, role, year in zip(names, roles, years_experience):
    if year >= 5:
        print(f"\n{name:<25} {year:<5}")
