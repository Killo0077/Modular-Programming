import random


def get_party_details():
    name = input("What is the child's name?: ")

    while True:
        try:
            number_of_children = int(input("How many children are invited? "))
            if number_of_children > 0:
                break
            else:
                print("Number must be greater than 0")

        except:
            print("Please enter a valid number")

    return name, number_of_children




def create_invoice(name, number_of_children):
    code = name[:2].upper() + str(random.randint(100, 999))

    cost = number_of_children * 22.50
    
    if number_of_children > 15:
        cost = cost * 0.90
        invoice = f"""---invoice--- 
        name: {name}
        code: {code}
        Total cost: £{cost:.2f}"""

    else: 
        invoice = f"""---invoice--- 
        name: {name}
        Code: {code} 
        Total Cost: ${cost:.2f}"""

    return invoice



def main():
    name, num = get_party_details()
    invoice = create_invoice(name, num)
    print (invoice)

main()