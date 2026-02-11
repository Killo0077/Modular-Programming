# Task 2- Reading numbers from file

with open ("prices.txt") as connection:
    prices = [int(price) for price in connection]

# Determine and print the cost of the most expensive house
print(f"The most expensive house costs ${max(prices):,}")

# Determine and print the cost of the cheapest house
print(f"The most cheapest house cost $ {min(prices):,}")

# Determine and print the average cost of the houses
average = sum(prices) / len(prices)
print(f"The average house cost $ {average:,.0f}")

# Write the prices in reverse order into a file called "dearest_to_cheapest.txt"
prices.sort(reverse= True)
with open ("dearest_to_cheapest.txt", "w") as output:
    for price in prices:
        print(price, file=output)
        