prompt = "\nIf you could visit one place in the world, where would you go? "
prompt += "\nEnter 'quit' to end the program.  "

places = {}

while True:
    name = input("What is your name? ")
    place = input(prompt)

    places[name] = place

    repeat = input("Do you want to continue? (yes/ no)")
    if repeat == 'no':
        break

print('\n')
for name, place in places.items():
    print(name + " want to visite " + place + ".")