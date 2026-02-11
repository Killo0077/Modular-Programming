# Task 2, Second solution

prices = []

with open("prices.txt") as prices_file:
    for line in prices_file:
        prices.append(int(line))

# Determine and print the cost of the most expensive house
print(f"The most expensive house costs ${max(prices):,}")

# Determine and print the cost of the cheapest house
print(f"The cost cheapest house ${min(prices):,}")

# Determine and print the av erage cost of the houses
average = sum(prices) / len(prices)
print(f"The average house cost $ {average:,.0f}")

# Write the prices in reverse order into a file called "dearest_to_cheapest.txt"
prices.sort (reverse= True)
with open ("dearest_to_cheapest.txt", "w") as output:
    for k in range(len(prices)):
        print(prices[k], file=output)