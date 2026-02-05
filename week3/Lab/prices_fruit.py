# 4. Modify to read a third value into a third list.

fruits = []
quantities = []
prices = []

# Read the file
with open("prices.txt","r") as file:
    for line in file:
        data = line.strip().split(",")

        fruits.append(data[0])              #fruit name
        quantities.append(int(data[1]))     #quantities
        prices.append(float(data[2]))       #price

# Display table
print("Fruit                             Qty              Price")
print("------------------------------------------------------------")

for i in range(len(fruits)):
    print(fruits[i],"                       \t",quantities[i],"     \t",   prices[i])

# Most expensive fruit (highest price)
highest_price = max(prices)
index = prices.index(highest_price)

print("\nMost expensive fruit: ", fruits[index])

# Total stock value
total = 0

for i in range(len(fruits)):
    total = total + quantities[i] * prices[i]

print("\nTotal stock value: ",total,"\n")


