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


# Option 2: Delete a record
def delete_player(ids, gdpr, days, status):
    player_id = input("Enter ID to delete: ").strip()

    if player_id not in ids:
        print("Player not found")
        return
    
    index = ids.index(player_id)

    del ids[index]
    del gdpr[index]
    del days[index]
    del status[index]

    print(f"{player_id} deleted sucessfully")

# Option 3: Add a new record
def add_player(ids, gdpr, days, status):
    new_id = input("Enter new player ID: ").strip()

    if new_id in ids:
        print("ID already exists")
        return
    
    ids.append(new_id)
    gdpr.append("No")
    days.append(0)
    status.append("Active")

    print(f"{new_id} added successfully")

# Option 4: Update Status
def update_status(ids, status):
    player_id = input("Enter player ID: ").strip()

    if player_id not in ids:
        print("ID not found")
        return
    
    index = ids.index(player_id)

    new_status = input("Enter new status (Active/Locked/Disable): ")

    status[index] = new_status
    
    print(f"{player_id} updated successfully")

#------------------------------------------------------------------#
# Option #: Show players inactive more than 60 days
def show_inactive(ids, gdpr, days, status):
    print("\nInactive players (>60 days)")
    print("-" * 40)

    for i in range(len(ids)):
        if days[i] > 60:
            print(ids[i], gdpr[i], days[i], status[i])


# Option #: Show only Active players
def active_players(ids,gdpr, days, status):
    print("Show active players")
    print("------------")

    for i in range(len(ids)):
        if status[i] == "Active":
            print(ids[i], gdpr[i], days[i], status[i])


# Option #: Player with highest days max
def player_highest_days(ids,days):
    print("Player with highest day played")

    max_days = days[0]
    index = 0

    for i in range(len(days)):
        if days[i] > max_days:
            max_days = days[i]
            index = i
        
    print(ids[index], days[index])


# Option #: Lock inactive accounts (>90 days)
def inactive_account (ids,days,status):
    for i in range(len(ids)):
        if days[i] > 90:
            status[i] = "Locked"
    
    print("Inactive accounts over 90 days have been locked.")


# Option # : Search for a player
def search_player(ids, gdpr, days, status):
    player_id = input("Enter ID: ").strip()

    if player_id in ids:
        i = ids.index(player_id)
        print(ids[i], gdpr[i], days[i], status[i])
    else:
        print("Not found")


# Option #: Reset days to 0 
def reset_days_played(ids, days):
    player_id = input("Enter ID: ").strip()

    if player_id in ids:
        i = ids.index(player_id)
        days[i] = 0
        print(f"Days reset to 0 for {player_id}")
    else:
        print("Not found")

# Option # : Count how many locked players
def count_locked(ids, status):
    count = 0

    for i in range(len(ids)):
        if status[i] == "Locked":
            count += 1

    print("Total Locked players: ", count)


# 











# Option 8: Quit & Save
def save_file(ids, gdpr, days, status):
    with open("datalist.txt", "w") as file:
        for i in range(len(ids)):
            file.write(f"{ids[i]}, {gdpr[i]}, {days[i]}, {status[i]}\n")

    print("Data saved successfully")




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
            delete_player(ids, gdpr, days, status)
        elif choice == "3":
            add_player(ids, gdpr, days, status)
        elif choice == "4":
            update_status(ids, status)
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == '7':
            pass
        elif choice == "8":
            save_file(ids, gdpr, days, status)
            8

            break
        else:
            print("Invalid choice.")
        


if __name__ == '__main__':
    menu()
    