# Question 2: Access Control Display


def check_access_level(access = "Standar"):
    if access == "Admin":
        print("Administrator access")
    elif access == "Technician":
        print("Technician access")
    else:
        print("Standard access")

check_access_level("Manager")
check_access_level("Admin")
check_access_level()


