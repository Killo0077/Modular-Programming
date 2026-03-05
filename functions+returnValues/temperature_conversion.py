# Exercise 1 — Temperature conversion

# Write a function that converts Celsius to Fahrenheit.


# Formula: 
# F = (C × 9/5) + 32

def celsius_to_fahrenheit (celsius : float) -> float:
    fahrenheit = (celsius * 9/5) + 32

    return fahrenheit

if __name__ == "__main__":
    print(celsius_to_fahrenheit(20))    ## <- value 20 celsius to convert to fahrenheit test