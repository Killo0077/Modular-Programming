
def flowers_details():
    name = input("What is the flower name: ")

    while True:
        price = float(input("What is the price: "))
        if price > 0:
            break
        else: 
            print("Price must be greater than 0")

    return name, price



def calculate_order(name, cost):
    total = cost * 10

    if cost <= 4:
        delivery = 10
    else:
        delivery = 15

    total += delivery

    return f"Order: 10 {name} stems\ncost: $ {total:.2f}"

def main():
    name, cost = flowers_details()
    print(calculate_order(name, cost))

main()