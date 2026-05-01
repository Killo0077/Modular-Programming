# Loop with index
for i in range(len(ids)):
    print(ids[i])


# Search
if player_id in ids:
    index = ids.index(player_id)
    print(ids[index], paid[index], days[index], status[index])
else:
    print("Not found")


# Filter
for i in range(len(ids)):
    if days[i], paid[i], days[i], status[i]

# Count
count =0
for i in range(len(ids)):
    if ids[i].startswith("PRO"):
        count += 1
print(count)

# Max
max_value = days[0]
index_max = 0

for i in range(len(days)):
    if days[i] > max_value:
        max_value = days[i]
        index_max = 1

print(ids[index_max])

# Delete
index = ids.index(player_id)
del ids[index]
del paid[index]
del days[index]
del status[index]

# Add
ids.append(new_id)
paid.append("No")
days.append(0)
status.append("Active")

# Update
index = ids.index(player_id)
status[index] = "Active"

# File write
with open("file.txt", "w") as f:
    for i in range(len(ids)):
        f.write(f"{ids[i]},{paid[i]},{days[i]},{status[i]}\m")

