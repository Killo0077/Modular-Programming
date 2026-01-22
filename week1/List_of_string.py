#


countries = ["spain", "brazil", "portugal", "bolivia", "ireland", "italy"]

print(countries)

for i in range(len(countries)):
    countries[i] = countries[i].title()

print(countries)

countries.append("Australia")
print(countries)

countries.insert(2, "Iceland")
print(countries)

countries.remove("Bolivia")
print(countries)


country = input("Country to add:").title()

while country in countries:
    country = input("country to add: ").title

countries.append(country)
print(countries)


count = 0

for i in range(len(countries)):
    if countries[i][0] == "I":
        count += 1
        print(count)
