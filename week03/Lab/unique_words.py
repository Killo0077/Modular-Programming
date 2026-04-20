# 5. Remove duplicate words

unique_words = []

# Read the file
with open("duplicate_list.txt","r") as file:
    for line in file:
        word = line.strip()

        if word not in unique_words:
            unique_words.append(word)

print(unique_words)

# Write back to the file (overwrite old content)

with open("duplicate_list.txt","w") as file:
    for word in unique_words:
        file.write(word + "\n")

print("Duplicate word removed.")
print(unique_words)