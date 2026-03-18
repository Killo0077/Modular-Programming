

def get_birthday() -> tuple[str, int]:
    """
    :param :name of person birthday
    :param: age of person on birthday 
    :return: name and age
    """
    name: str = input("Enter first name: ")
    age: int = int(input("Enter your age: "))

    return name, age


def main():
    name, age = get_birthday()
    print(f"Happy Birthday {name}! You are {age} years old.")

if __name__ == "__main__":
    main()
