
month = ["April", "May", "June","July", "August", "September"]
celsius = [15,19,24,31,31,29]

print("Month            Celsius")
print("-------------------------")

for i in range(len(month)):
    if celsius[i] >= 29:
        print(f"{month[i]:<20}{celsius[i]:<5} heatwave")
    else:
        print(f"{month[i]:<20}{celsius[i]:<5}")


count_below = 0
count_above = 0

for c in celsius:
    if c <= 20:
        count_below += 1
    else:
        count_above += 1

print(f"\n20 degrees or below: {count_below} months.")
print(f"Over 20 degrees: {count_above} months")



max_val = max(celsius)

print("\nThe hottest month(s): ")

for i in range(len(celsius)):
    if celsius[i] == max_val:
        print(month[i])
