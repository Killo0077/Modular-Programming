import random

def patient_info():
    year = int(input("What is the year of admission: "))

    while True:
        city_of_residence = input("What is your city of residence: ")
        if city_of_residence != "":
            break
        else: 
            print("City of residence can not be empty")
            
        
    return year, city_of_residence


def generate_patient_id(year, city):
    patient_id = city[:2] + str(int(year)) + str(random.randint(4,99))
    return patient_id





def main():
    year, city_of_residence = patient_info()
    patient_id = generate_patient_id(year, city_of_residence)

    print("Year: ", year)
    print("City: ", city_of_residence)
    print("Patient ID: ", patient_id)

main()