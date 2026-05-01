# Gamer Account System
# Author: Pablo Baena
# MTU Modular Programming / Project, March- April 2026

def read_file(filename):
    ids = []    # list  of players
    paid = []   # Yes/No for subscriptions
    days = []   # numbers of days since last login
    status = [] # Active/ Locked / Disable

# Read the gamers.txt file and store each column in a separate list
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            ids.append(parts[0])
            paid.append(parts[1])
            days.append(int(parts[2]))
            status.append(parts[3])

    return ids, paid, days, status


# Option 1: Print a formatted table of all players including account type
def view_all_players(ids, paid, days, status):
    print("\nID\t\tType\tPaid\tStatus\tAlert")
    print("-" * 50) # ------------------------------.....
    
    for i in range(len(ids)):
        # Account type
        if ids[i].startswith("CAS"):
            account_type = "Casual"
        else:
            account_type = "Pro"
        
        #Paid symbol
        if paid[i] == "Yes":
            paid_symbol = "\u2705"
        else:
            paid_symbol = "\u274E"

        # Alert for >90 days
        alert = "\U0001F6AB" if days[i] > 90 else""

        print(f"{ids[i]:<10} {account_type:<8} {paid_symbol:<5} {days[i]:<6} {status[i]:<10} {alert:5}")


# Option 2: Delete a record, all data associated with the record along with an appropiate success message
def delete_player(ids, paid, days, status):
    player_id = input("Enter the ID to delete ")

    if player_id not in ids:
        print("ID not found. Please enter a valid ID")
        return
    # find the index of the record
    index = ids.index(player_id)

    # delete from all lists
    del ids[index]
    del paid[index]
    del days[index]
    del status[index]

    print(f"Player {player_id} deleted successfully.")

# Option 3: Add a new player
def add_player(ids, paid, days, status):
    print("\n----- Add New Player ------")

    new_id = input("Enter new player ID: ").strip()

    #Check if ID already exists
    if new_id in ids:
        print("This ID already exists.")
        return
    
    ids.append(new_id)
    paid.append("No")
    days.append(0)
    status.append("Active")

    print(f"Player {new_id} added successfully.")
    
    
   
# Option 4: Update Status
def update_status(ids, status):
    print("\n--------- Update Player Status --------")

    player_id = input("Enter the player ID to update: ")

    if player_id not in ids:
        print("ID not found.")
        return
    
    index = ids.index(player_id)
    
    print("Choose new status:")
    print("1. Active")
    print("2. Locked")
    print("3. Disable")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        status[index] = "Active"
    elif choice == "2":
        status[index] = "Locked"
    elif choice == "3":
        status[index] = "Disable"
    else:
        print("Invalid choice")
        return
    
    print(f"Status for {player_id} updated sucessfully.")


def inactive_players(ids, status):
    


# Option 8: Quit & Save
def save_file(ids, paid, days, status):
    with open("gamers.txt", "w") as file:
        for i in range(len(ids)):
            file.write(f"{ids[i]},{paid[i]},{days[i]},{status[i]}\n")
        
    print("Data saved successfully, Bye!")





def menu():
    filename = "gamers.txt"
    ids, paid, days, status = read_file(filename)
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
        
        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("Option 1 selected")
            view_all_players(ids, paid, days, status)

        elif choice =="2":
            print("Option 2 selected")
            delete_player(ids, paid, days, status)

        elif choice =="3":
            print("Option 3 selected")
            add_player(ids, paid, days, status)

        elif choice =="4":
            print("Option 4 selected")
            update_status(ids, status)
            
        elif choice =="5":
            pass
        elif choice =="6":
            pass
        elif choice =="7":
            pass
        elif choice =="8":
            print("Option 8 selected")
            save_file(ids, paid, days, status)
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    menu()


    
    