



def get_level(session):
    if session < 5:
        return "Low"
    elif session < 10:
        return "Medium"
    else:
        return "Hight"
    

def hight_members(names,sessions):

    result = []

    for i in range (len(names)):
        if sessions[i] > 10:
            result.append(names[i])

    return result
        

    

def main():
    names = ["Ana", "Luis", "Carlos", "Marta"]
    sessions = [3, 12, 8, 15]

    name = input("Enter a member name: ")
    session = int(input("Enter number of session: "))

    names.append(name)
    sessions.append(session)

    print("\nName       Sessions        Level")
    print("-------------------------------- ")

    for i in range(len(names)):
        level = get_level(sessions[i])
        print(f"{names[i]:10} {sessions[i]:10} {level}")

    max_s = max(sessions)
    index = sessions.index(max_s)

    print("\nTop member: ", names[index])

    print("High members: ", hight_members(names, sessions))


if __name__ == "__main__":
    main()
