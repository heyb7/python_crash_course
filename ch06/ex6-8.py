pets = []

cat = {
    'type': 'cat',
    'owner': 'peter',
    'age': 8,
}
pets.append(cat)

dog = {
    'type': 'dog',
    'owner': 'john', 
    'age': 5,
}
pets.append(dog)

pig = {
    'type': 'pig',
    'owner': 'lily',
    'age': 4,
}
pets.append(pig)

for pet in pets:
    print("\npet name: " + pet['type'])
    for key, value in pet.items():
        print('\t' + key + ': ' + str(value))