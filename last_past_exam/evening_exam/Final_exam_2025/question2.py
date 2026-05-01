
names = ["Oisin", "Cillian", "Niamh", "James", "Oleksandr","Omar", "Rian"]
stars = [12,45,60,33,22,75,50]

print("\nStarts Spotted")
print("-" *25)

for i in range(len(names)):
    if stars[i] < 50:
        percent = (stars[i] / 50) * 100
        print(f"{names[i]:<15}{stars[i]:<5}{percent:.0f}%")
    else:
        print(f"{names[i]:<15}{stars[i]:<5}")


total = 0
count = 0

for s in stars:
    if s < 50:
        total += s
        count += 1

if count > 0:
    avg = total / count
    print(f"\nThe average count was {avg:.2f} for those who counted less than 50.")

min_stars = min(stars)

print("\nThe least successful student(s): ")

for i in range(len(names)):
    if stars[i] == min_stars:
        print(names[i])