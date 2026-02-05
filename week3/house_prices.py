# Reading numbers from file into a list

# Write a program to read house prices from a file into a list of integers or floats

house_prices = []

with open("house_prices.txt") as h:
    for line in h:
        house_prices.append(int(line.strip()))
        print("The prices are: ", house_prices)

# Determine and print the cost of the most expecive house using max()

print("Most expensive house: ", max(house_prices))

# Determine and print the average cost of the houses using sum() and len()

average = sum(house_prices) / len(house_prices)

print("Average house price: ", average)

# Write the prices in decreasing order of price into a file called "dearest_to_cheapest.txt"

house_prices.sort()
print(house_prices)
