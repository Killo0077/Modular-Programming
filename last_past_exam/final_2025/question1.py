
import random


def patient_details():
    year_admision = input("Enter year admision: ")
    
    while True:
        city = input("Enter city of residence : ")
        if city != "":
            break
        else:
            print("Invalid input.Please enter a valid city ")

    return year_admision, city


def generate_patient_id(year_admission, city):
    patient_id = city[:2].upper() + year_admission + str(random.randint(1,9))
    return patient_id


def main():
    year, city = patient_details()
    patient_id = generate_patient_id(year,city)

    print("\n---- Patient Details ----")
    print("Year: ", year)
    print("city: ", city)
    print("Patient ID: ", patient_id)

main()
