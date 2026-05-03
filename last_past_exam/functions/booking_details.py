


def get_booking_details():
    customer_name = input("What is your name: ")

    while True:
        try:
            number_of_nights = int(input("How many nights: "))
            if 1 <= number_of_nights <= 14:
                break
            else:
                print("Number  of nights must be between 1 and 14")

        except:
            print("Plese enter a valid number")

    return customer_name, number_of_nights



def calculate_total_cost(nights):
    cost_per_night = 50
    total = nights * cost_per_night

    if nights > 7:
        total = total * 0.9 # 10% discount

    return total



def main():
    name, nights = get_booking_details()
    total_cost = calculate_total_cost(nights)

    print("\n---- Booking Details ------")
    print("Name: ", name)
    print("Nights: ",nights)
    print("Total Cost: $", total_cost)

main()