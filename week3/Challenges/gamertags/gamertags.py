### Week 3 - Challenges - Gamertags ######

FirstNames = []
LastNames = []
gamertags = []

with open("gamertags.txt", "r") as file:
    for line in file:
        line = line.strip()  # Remove newline
        parts = line.split(",")  # split by comma

        FirstNames.append(parts[0])
        LastNames.append(parts[1])
        gamertags.append(parts[2])

# Display neat table with row count
print("=" * 45)
print(f"\n{'Row':<4} {'First Name': <12} {'Last Name': <15}{'Gamertag'}")
print("=" * 45)

for i, (fname, lname, tag) in enumerate(zip(FirstNames, LastNames, gamertags), start=1):
    print(f"{i: <4} {fname:<12}{lname:<15}{tag}")
    print("-" * 45)

# Average lenght of a gamertag.

total_length = 0
for tag in gamertags:
    total_length += len(tag)

average = total_length / len(gamertags)
print("\nAverage gamertag length: ", round(average, 2))


# Ask for a name and display

search_name = input("\nEnter a first name to search: ")

if search_name in FirstNames:
    index = FirstNames.index.(search_name)
    print("Gamertag: ", gamertags[index])
else:
    print("Name not found.")
