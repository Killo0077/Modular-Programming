


def holidays() -> tuple[str, int]:
    """
    :return: name and size of group
    """
    name: str = input("Enter your name: ")
    number: int = int(input("Enter group size: "))

    return name, number

def get_discount(name: str, size: int) -> float:
    """
    :param name
    :param size of group
    :return discount to apply e.g. 0.05, 0.20 or 0.10
    """
    if size  > 4:
        return 0.20
    elif "a" in name.lower() or "o" in name.lower():
        return 0.10
    else:
        return 0.05
    

def get_destinations () -> list[str]:
    """
    :return list of destination
    """
    destinations = []

    for i in range(5):
        place = input(f"Enter destination {i+1}:")
        destinations.append(place)

    return destinations


def get_flight_cost(destinations: list[str]) -> list[float]:
    """
    :param list of destinations
    :return list of flight costs
    """

    costs = []
    for place in destinations:
        price = float(input(f"Enter flight cost for {place}:"))
        costs.append(price)
    
    return costs

def display_final_prices(destinations: list[str], costs: list[float], discount: float) -> None:
    print("\n--- Final Prices ---")

    for i in range(len(destinations)):
        final_price = costs[i] - (costs[i] * discount)

        print(f"{destinations[i]}: Original £{costs[i]:.2f} → Discounted £{final_price:.2f}")




def main():
    name, number = holidays()
    
    discount = get_discount(name, number)
    destinations = get_destinations()
    costs = get_flight_cost(destinations)
    
    display_final_prices(destinations, costs, discount)
    # print("\nDestinations:", destinations)
    # print("Costs:",costs)

    # print(f"\nDestinations: {destinations}")

    # print (f"Discount: {discount * 100}%")    
    # print(f"{name} is travelling with a group of {number}")







if __name__ == "__main__":
    main()