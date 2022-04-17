import requests

req = requests.get("https://swapi.dev/api/people/27")
person = req.json()

print(f"Name: {person['name']}")
print(f"Height: {person['height']}")
print(f"Mass: {person['mass']}")
print(f"Birth Year: {person['birth_year']}")

req = requests.get(person['homeworld'])
homeworld = req.json()

print(f"Homeworld: {homeworld['name']}")