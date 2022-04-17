import json

person = '''
    {
        "name": "Ackbar", 
        "height": "180", 
        "mass": "83", 
        "hair_color": "none", 
        "skin_color": "brown mottle", 
        "eye_color": "orange", 
        "birth_year": "41BBY", 
        "gender": "male", 
        "homeworld": "https://swapi.dev/api/planets/31/", 
        "films": [
            "https://swapi.dev/api/films/3/"
        ], 
        "species": [
            "https://swapi.dev/api/species/8/"
        ], 
        "vehicles": [], 
        "starships": [], 
        "created": "2014-12-18T11:07:50.584000Z", 
        "edited": "2014-12-20T21:17:50.362000Z", 
        "url": "https://swapi.dev/api/people/27/"
    }
'''

person = json.loads(person)
person['name'] = "Rabkca"
new_person = json.dumps(person)

print(new_person)