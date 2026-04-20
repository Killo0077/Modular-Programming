

country_list = ["Iceland", "India", "China", "Japan", "France", "Ireland", "Ukraine" ]

# 1. Create a copy of this list using list comprehension.
country_list = country_list[:]

# 2. Create a list that only contains countries beginning with "I"
countries_starting_with_I =[
    country for country in country_list if country.startswith("I")
]
print(countries_starting_with_I)


# 3. Create a list that only contains countries ending in 'a'
country_ended_a =[
    country for country in country_list if country.endswith("a")
]
print(country_ended_a)


# 4. Create a list that contains the first three letters of each country in capitals.
first_3_letters = [
    country[:3].upper() for country in country_list
]
print(first_3_letters)

# 5. Create a list that only contains 5 letter countries.
five_letters= [
    country for country in country_list if len(country) == 5
]
print(five_letters)

# 6. Ask the user to enter a letter- show a list of countries that contain this letter but don't start with that letter.
letter = input ("Please type a letter \n")

result = [
    country for country in country_list
    if letter in country and not country.startswith(letter)
]

print (result)