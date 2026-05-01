while True:
    value = float(input("Enter value: "))
    if value > 0:
        break
    else:
        print("Value must be greater than 0")


# for integer:
while True:
    try:
        value = int(input("Enter number: "))
        if value > 0:
            break
        else:
            print("Number must be greater than 0")
    except:
        print("Enter a valid number")