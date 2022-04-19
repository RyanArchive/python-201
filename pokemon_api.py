import requests

while True:
    pokemon_name = input("Enter pokemon name: ")
    pokemon_name = pokemon_name.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    req = requests.get(url)

    if req.status_code == 200:
        pokemon = req.json()

        print(f"\nPokemon Name: {pokemon['name'].capitalize()}")
        print(f"Base Experience: {pokemon['base_experience']}")
        print(f"Types:")
        for index, type in enumerate(pokemon['types']):
            print(f"\t{pokemon['types'][index].get('type').get('name').capitalize()}")
        print(f"Abilities:")
        for index, ability in enumerate(pokemon['abilities']):
            print(f"\t{pokemon['abilities'][index].get('ability').get('name').capitalize()}")
        print("")
        
    else:
        print("\nPokemon not found.\n")

    again = None

    while True:
        again = input("Do you want to search again? [y/n] ")
        again = again.lower()

        if again == 'y':
            break
        elif again == 'n':
            exit()