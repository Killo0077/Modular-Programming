import random

def get_product_details():
    product_name = input("What is the product name: ")

    while True:
        try:
            product_price = float(input("How much cost it: "))
            if product_price > 0:
                break
            else:
                print("Product price must be greater than zero : ")

        except:
            print("Please enter a valid number")

    return product_name, product_price
    

def generate_product_code(name, price):
    product_code = name[:2].upper() + str(int(price)) + str(random.randint(10,19))
    return product_code





def main():
    product_name, product_price = get_product_details()
    product_code = generate_product_code(product_name, product_price)

    print("Name: ", product_name)
    print("Price: ", product_price)
    print("Code: ", product_code)

main()