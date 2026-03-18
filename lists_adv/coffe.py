# You are tasked with developoing a python application that analyses coffee shop sales for different types of 
# coffee drinks sold.


# The data file 

# coffee name, number of cups sold, price per cup 

def data_coffee(filename): 
    """
:param file name: the name of the file containing the sales data
:return: three lists -list of coffee names, list of numbers of cups sold and lists of prices per cup"""
    coffees = []
    solds = []
    prices = []

    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(',')

                coffees.append(parts[0])
                solds.append(int(parts[1]))
                prices.append(float(parts[2]))

                if len(coffees) == 0:
                    print("File is empty")

    except FileNotFoundError:
        print("File not found")

    return coffees, solds, prices

def display_table(coffees, solds, prices):
    print("\n-----COFFEE SALES ----")
    print("Name\t\tCups\tPrices\tMarker")

    for i in range(len(coffees)):
        marker = ""

        if solds[i] > 100:
            marker = "*"
        
        print(f"{coffees[i]:12}{solds[i]:8}{prices[i]:8}{marker}")

def total_earnings(solds, prices):
    """
    :param cups sold: list of number of cups solds(integers)
    :param prices: list of prices per cup (float)
    :return: total earnings (float)"""
    total = 0

    for i in range(len(solds)):
        total += solds[i] * prices[i]
    
    return total

def highest_sales(coffees, solds):
    """
    :param coffee: list of coffee names
    :param solds: list of cups solds
    :return: list of coffees with highest sales"""
    result = []

    max_value = max(solds)

    for i in range(len(coffees)):
        if solds[i] == max_value:
            result.append(coffees[i])
        
    return result

def highest_price(coffees, prices):
    """
    :param coffees: list of coffee names
    :param prices: list of prices per cup
    :return: list of coffees with highest price"""
    result = []
    max_value = max(prices)
    for i in range(len(coffees)):
        if prices[i] == max_value:
            result.append(coffees[i])
        
    return result

# def change_price (percentage, prices):
#     for k in range(len(prices)):
#         prices[k] = prices[k] + percentage * prices [k]


def main ():
    coffees, solds, prices = data_coffee("coffee_sales.txt")
    
    display_table(coffees, solds, prices)

    total = total_earnings(solds, prices)
    print(f"\nTotal earnings: $ {total}")

    result = highest_sales(coffees, solds)
    print(f"\nThe hightest sales :{result}")

    # change_price(0.1, solds)
    # print_table(coffees, solds, prices)

   

if __name__ == "__main__":
    main()