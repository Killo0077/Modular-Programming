
plant_id = [1,2,3,4,5]
humidity = [40,60,75,30,85]
sunlight_hours = [5,3,8,4,10]

print("Plant ID     Humidity(%)     Sunlinght Hours")
print("-"*70)

poor_count = 0

for i in range(len(plant_id)):

    score = (humidity[i] * 0.5) + (sunlight_hours[i] * 2)

    if score < 50:
        category = "Poor"
        poor_count += 1
    elif score <= 80:
        category = "Moderate"
    else:
        category = "Optimal"

    print(f"{plant_id[i]:<10}{humidity[i]:<15}{sunlight_hours[i]:<20}{score:<10.2f}{category}")

percentage = (poor_count / len(plant_id)) * 100
print(f"\nPercentage of plants in 'Poor' category: {percentage:.1f} %")
