# zip() is used throughout this program because it works well with multiple lists.
# Each funtionality could be implemented without zip() as demostrated in some snippets of code.

f = open("stock2.txt")

fruits =[]
stocks =[]
costs =[]

for line in f:
    fruit, stock, cost = line.split(',')
    fruits.append(fruit.title())
    stocks.append(int(stock))
    costs.append(float(cost))

f.close()

######################################################
# display the data on the screen in a neat table.

print(f"{'Fruit':24}{'Quantity':<10}{'Cost'}")
print('-' * 50)
for fruit, stock, cost in zip (fruits, stocks, costs):
    print(f"{fruit:24}{stock:<10}{cost:.2f}")
print()

#######################################################
most_expensive = max(costs)
# Create a list of the most expensive fruits - this is wasteful because we don't use the list for 
# anything else but I am providing it anyway
fruits_most_expensive = [fruit for fruit, cost in zip(fruits, costs) if cost == most_expensive]
print(f"The most expensive fruits are:  {' and '.join(fruits_most_expensive)}")
print()

# Using zip()
print(f"The most expensive fruits are:")
for item, price in zip(fruits, costs):
    if price == most_expensive:
        print(f"-{item}")

########################################################################################################
# determine the value of the stock
# Version 1 - create list of the value of each fruit. Use sum() to add them.
total  = sum([stock * cost for stock, cost in zip(stocks, costs)])
print(f"The stock is valued at €{total:,.2f}")

#  version 2 using zip()
total = 0
for stock, cost in zip(stocks, costs):
    total += stock * cost
print(f"The stock is valued at €{total:,.2f}")


########################################################################################################
# print the fuits beginning with 'G'
# This creates a list of the fruits starting with 'G' then joins them into one string, each fruit
# separated by the string ' and '.
gs = " and ".join([fruit for fruit in fruits if fruit[0] == 'G'])
print("The following fruits begin with 'g':", gs)
print()