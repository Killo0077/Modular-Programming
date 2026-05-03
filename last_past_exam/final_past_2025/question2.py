


humidity = [40,60,75,30,85]
sunlight_hours = [5,3,8,4,10]

print(f"{"humidity(%)":<20}{"Sunlight Hours":<20}{"Score":<15}{"Category"}")
print("-"*80)

count_poor = 0

for i in range(len(humidity)):

    score = (humidity[i] * 0.5) + (sunlight_hours[i] * 2)
    
    if score < 50:
        grade = "Poor"
    elif 50 <= score <= 80:
        grade = "Moderate"
    else:
        grade = "Optimal"

    if grade == "Poor":
        count_poor += 1

    print(f"{humidity[i]:<20}{sunlight_hours[i]:<20}{score:<15.2f}{grade}")

percentage = (count_poor / len(humidity)) * 100

print(f"\nPercentage of plants in 'Poor' category: {percentage:.1f}%")

