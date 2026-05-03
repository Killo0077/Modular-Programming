

def sandwich_menu(filename):
    ingredientA = []
    ingredientB = []
    price = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            ingredientA.append(parts[0])
            ingredientB.append(parts[1])
            price.append(float(parts[2]))

    return ingredientA, ingredientB, price




def sandwich_definition(ingredientA, ingredientB, price):

    print(f"{"Code":<10}{"Ingredient":<25}{"Cost One":<15}{"Cost two"}")
    print("-"*70)

    for i in range(len(ingredientA)):
        code = ingredientA[i][0] + "&"+ ingredientB[i][0]
        ingredients = ingredientA[i] + " & " + ingredientB[i]
        cost_of_one = price[i] 
        cost_of_two = price[i] * 2 * 0.8

        print(f"{code:<10}{ingredients:<25}{cost_of_one:<15.2f}{cost_of_two:.2f}")



def find_sandwich(search, ingredientA, ingredientB):

    result = []

    for i in range(len(ingredientA)):
        if search.lower() == ingredientA[i].lower() or search.lower == ingredientB[i].lower():
            sandwich = ingredientA[i] + " and " + ingredientB[i]
            result.append(sandwich)

    return result


def main():
    ingredientA, ingredientB, prices = sandwich_menu("sandwiches.txt")

    sandwich_definition(ingredientA, ingredientB, prices)

    search = input("\nEnter ingredient to search:  ")
    print(f"\nThe following sandwiches have {search}: ")

    matches = find_sandwich(search, ingredientA, ingredientB)

    for sandwich in matches:
        print("-", sandwich)

main()