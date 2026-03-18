# The Data is stored in a file containing comma separated values




def store_data(filename):
    """
    :param filename: the name of the file containing the sales data
    :return: three lists - list of t-shirt names, list of number of units sold and list of prices per unit
    """
    names= []
    units_solds = []
    prices = []


    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(',')

                names.append(parts[0])
                units_solds.append(int(parts[1]))
                prices.append(float(parts[2]))

            if len(names) == 0:
                print("file is empty")

    except FileNotFoundError:
        print("File not found")   

    return names,units_solds,prices

def display_data(names, units_solds, prices):
    """
    :param t-shirt names: list of t-shirt types (string)
    :param units sold: list of number of units sold (intergers)
    :param prices per unit: list of prices per unit (float)
    :param bad sales: a number which is deemed to be poor sales figure (int) default value 150
    :return: None
    """
    print("\n-------T-shirt Store-------")
    print(f"{'Name':18}{'Unit Sales':12}{'Price':18}{'Bad Sales':10}")

    for i in range(len(names)):
        stored = ""

        if units_solds[i] < 150:
            stored = "Bad" 

        print (f"{names[i]:18}{units_solds[i]:12}{prices[i]:10.2f}{stored:10}")


def analyse(names,units_solds,prices):
    """
    :param t-shirt names: list of t-shirt types (string)
    :param units sold: list of number of units sold (integers)
    :param prices per unit: list of prices per unit (float)
    :return: t-shirt name with the largest value of sales (list of string)
    """
    values = []

    for i in range(len(units_solds)):
        values.append(units_solds[i] * prices[i])

    max_value = max(values)

    result = []

    for i in range(len(names)):
        if values[i] == max_value:
            result.append(names[i])
       
    return result





def main():
    names,units_solds, prices = store_data ("data_store.txt")
    
    display_data(names,units_solds,prices)
    
    result = analyse(names, units_solds,prices)
    print(f"\nHightest value sales: {result}")
    

if __name__ == "__main__":
    main()