# excercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys,values)))
# excercise 2
# family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
# total_price = 0

# for name, age in family.items():
family = {}
total_price=0
while True:
    name = input("Enter name ( end to exit): ")
    if name == "end":
        break
    age = int(input("Enter an age: "))
    family[name] = age
    if age < 3:
     ticket = 0
    elif age < 12:
        ticket = 10
    else:
        ticket=15

    total_price += ticket
    print(f"{name} {age}yrs old must pay ${ticket}")

print("The total is $",total_price)
# excercise 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

brand["number_stores"] = 2
print(f"Zara clients are {brand['type_of_clothes']}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(f"Major colors in US are: {brand['major_color']['US']}")
print(len(brand))
print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}

brand.update(more_on_zara)
print("there are",brand["number_stores"],"stores")


# excercise 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
ex1 = {}
for index in range(len(users)):
    ex1[users[index]] =index
print(ex1)
ex2 = {}
for index in range(len(users)):
    ex2[index] = users[index]
print(ex2)
ex3 = {}
sorted_users = sorted(users)
for index in range(len(sorted_users)):
    ex3[sorted_users[index]] = index
print(ex3)
ex4 = {}
for index in range(len(users)):
    if "i" in users[index]:
        ex4[users[index]] = index
print(ex4)
ex4ii = {}
for index in range(len(users)):
    if users[index][0] in ["M", "P"]:
        ex4ii[users[index]] = index
print(ex4ii)