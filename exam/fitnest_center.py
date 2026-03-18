# A fitness center stores , member has: name, number of workout complete in a month

# The Data is stored in a file containing comma separated values




def get_workout(filename):
    """
    :param filename: the name of the file containing the sales data
    :return: three lists - list of t-shirt names, list of number of units sold and list of prices per unit
    """
    names= []
    workouts = []
    
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(',')

                names.append(parts[0])
                workouts.append(int(parts[1]))
                
            if len(names) == 0:
                print("file is empty")

    except FileNotFoundError:
        print("File not found")   

    return names,workouts


# display data
def display_data(names, workouts):
    """
    :param list of names (string)
    :param numbers of workouts (intergers)
    :return: None
    """
    print("\n-------Fitnes Club-------")
    print(f"{'Name':18}{'Workout':12}")

    for i in range(len(names)):
        # stored = ""

        # if workouts[i] < 150:
        #     stored = "Bad" 

        print (f"{names[i]:18}{workouts[i]:12}")

# count how many members completed more workout

def analyse(names,workouts):
    """
    :param names list(string)
    :param workout list (integers)
    :return: names and workout list (list of string)
    """
    # values = []

    # for i in range(len(workouts)):
    #     values.append(names[i] * workouts[i])

    # max_value = max(values)

    # result = []

    # for i in range(len(names)):
    #     if values[i] == max_value:
    #         result.append(names[i])
       
    # return result
    max_value = max(workouts)
    result = []

    for i in range(len(names)):
        if workouts[i] == max_value:
            result.append(names[i])

        return result
    


def display_fitness_categories(names,workouts):
    """
    :param names  (string)
    :param number of workouts (intergers)
    :param categoria Beginner (integer)
    :param categoria Intermediate (integer)
    :param categoria Advanced (integer)
    :return: None
    """
    print("\n-------Fitnest Club Categories-------")
    print(f"{'Name':18}{'Workout':12}{'Categoria':18}")

    for i in range(len(names)):
        # categorias = ""

        # if workouts[i] > 10:
        #     categorias = "Beginner"
        # elif workouts [i] > 10:
        #     categorias = "Intermediate"
        # else:
        #     categorias = "Advanced"
        for i in range(len(names)):
            if workouts[i] <= 5:
                category = "Beginner"
            elif workouts [i] <= 10:
                category = "Intermediate"
            else:
                category = "Advanced"



    print (f"{names[i]:18}{workouts[i]:12}{category[i]:10}")

def main():
    names,workouts = get_workout ("data_fitnest.txt")
      
    display_data(names,workouts)

    # Didn't added
    result = analyse(names,workouts)
    print(f"\nMost workouts: {result}")

    display_fitness_categories(names,workouts)
      
     
        
    
    

if __name__ == "__main__":
    main()

































