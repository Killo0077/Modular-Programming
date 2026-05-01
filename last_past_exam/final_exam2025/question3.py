
def hotel_prices(filename):
    hotel_name = []
    cost_per_night = []
    dinner_cost = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            hotel_name.append(parts[0])
            cost_per_night.append(float(parts[1]))
            dinner_cost.append(float(parts[2]))

    return hotel_name, cost_per_night, dinner_cost



def pricing_info(hotel_name, cost_per_night, dinner_cost):
       
    print("Name     Code    cost for 5 nights + dinner")
    print("-"*40)

    for i in range(len(hotel_name)):

        code = hotel_name[i][:2].upper()

        total = (cost_per_night[i] + dinner_cost[i]) * 5

        if cost_per_night[i] > 200:
            reduce = total * 0.8
            print(f"{hotel_name[i]:<10}{code:<5}$ {total:.0f} reduce to $ {reduce: .0f}")
        else:
            print(f"{hotel_name[i]:<10}{code:<5}$ {total:.0f}")

def get_hotels_in_range(low, hight, names, prices):
    result = []

    for i in range(len(names)):
        if low <= prices[i] <= hight:
            result.append(names[i])

    return result

def main():
    names, prices, dinners = hotel_prices("hotels.txt")
    pricing_info(names, prices,dinners)

    result = get_hotels_in_range(100,180, names, prices)

    print("\nHotels with a night rate between 100 and 180 inclusive: ")
    for hotel in result:
        print(hotel)


main()



