person = [("name", "Ryan"), ("gender", "male")]

d_person = {}
for key, value in person:
    d_person[key] = value
print(d_person)

d_person = {key: value for key, value in person}
print(d_person)

d_person = dict(person)
print(d_person)