def get_items_in_range(low, high, names, values):
    result = []

    for i in range(len(names)):
        if low <= values[i] <= high:
            result.append(names[i])

    return result