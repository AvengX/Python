import json

cities_data = {
    "Mumbai": 20000000,
    "Delhi": 19000000,
    "Bangalore": 12000000
}

with open("cities.json", "w") as f:
    json.dump(cities_data, f, indent=4)

with open("cities.json", "r") as f:
    loaded_data = json.load(f)

for city, pop in loaded_data.items():
    print(f"{city}: {pop}")

new_city = input("\nEnter a new city: ")
new_pop = int(input(f"Enter population for {new_city}: "))

loaded_data[new_city] = new_pop

with open("cities.json", "w") as f:
    json.dump(loaded_data, f, indent=4)