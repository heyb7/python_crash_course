prompt = "\nEnter you age: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("free ticket.")
    elif age < 12:
        print("10$ ticket.")
    else:
        print("15$ ticket.")
