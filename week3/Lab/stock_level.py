# 3. Reading strings and numbers from file into 2 list 

fruits = []
stock_levels = []

# Open connection

with open("stock_level.txt") as s:
    for line in s:
        fruit, stock = line.strip().split(',')
        fruits.append(fruit)
        stock_levels.append(int(stock))

print(fruits)
print(stock_levels)

# Display the data on the screen in a neat table.

for i in range(len(fruits)):
    print(fruits[i], "----------------" , stock_levels[i])

# Determine the fruits(s) of which there is most stock

biggest_stock = max(stock_levels)
print("Most stock: ", biggest_stock)


print("\n")
# Print the fruits beginning with 'G'.

for fruit in fruits:
    if 'G' in fruit:
        print(fruit)