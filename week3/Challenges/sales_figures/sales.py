# Week 3- Challenge, Sales Figures

names = []
sales = []

# Read file
with open("sales_figures.txt","r") as file:
    for line in file:
        data = line.strip().split(",")
        names.append(data[0])
        sales.append(float(data[1]))

# Add late employee

late_name = input("Enter employee name: ")

while True:
    try:
        late_sales = float(input("Enter sales amount: "))
        break
    except:
        print("Enter a valid number. ")

names.append(late_name)
sales.append(late_sales)

# Total sales
total = sum(sales)
print("\nTotal weekend sales: ", total)

# Average
average = total / len(sales)
print("\n The average is: ",average,"$")

# Count below average
count = 0
for amount in sales:
    if amount < average:
        count += 1

print("\nEmployess below average: ",count)

# Highest sales
highest = max(sales)
index_high = sales.index(highest)

print("\nHighest sales: ",names[index_high])

# Create bonus file (3%)
with open("bonus.txt","w") as file:
    file.write("Name              Sales              Bonus\n")
    file.write("---------------------\n")

    for i in range(len(names)):
        bonus = sales[i] * 0.03
        file.write(names[i] + "    " + str(sales[i]) + "    " + str(round(bonus,2)) + "\n")

# Find lowest sales (after bonus file creation)
lowest = min(sales)
index_low = sales.index(lowest)

print("\nEmployee fired: ", names[index_low])

# Remove from list
names.pop(index_low)
sales.pop(index_low)

print("\n",names)



        