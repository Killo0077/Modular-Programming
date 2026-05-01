def load_file(filename):
    list1 = []
    list2 = []
    list3 = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            list1.append(parts[0])
            list2.append(float(parts[1]))
            list3.append(float(parts[2]))

    return list1, list2, list3