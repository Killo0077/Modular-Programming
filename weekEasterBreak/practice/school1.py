# Your name here...

def read_file(filename):
    ids = []
    gdpr = []
    days = []
    status = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            ids.append(parts[0])
            gdpr.append(parts[1])
            days.append(int(parts[2]))
            status.append(parts[3])

    return ids, gdpr, days, status

# Option 1: View all account data
def view_all_players(ids, gdpr,days, status):
    for i in range(len(ids)):

        if ids[i].startswith("CAS"):
            account_type = "Casual"
        else:
            account_type = "PRO"

        if gdpr[i] == "Yes":
            paid_symbol = "✔"
        else:
            paid_symbol = "❌"

        if days[i] > 90:
            alert = "🚨"    
        else:
            alert = ""

        print(ids[i], account_type, paid_symbol, status[i], alert)




def menu():
    filename = "datalist.txt"
    ids, gdpr, days, status = read_file(filename)
    choice = ""
    while choice != "8":
        print("\nMenu")
        print("1. View all players")
        print("2. Delete a player")
        print("3. Register new player")
        print("4. Update player status")
        print("5. Placeholder for Exam")
        print("6. Placeholder for Exam")
        print("7. Placeholder for Exam")
        print("8. Quit and save")
        choice = input("Enter choice: ")

        if choice == "1":
            view_all_players(ids, gdpr, days, status)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == '7':
            pass
        elif choice == "8":
            pass
            print("Data saved. Goodbye.")
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    menu()
    