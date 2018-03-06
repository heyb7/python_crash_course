prompt = "\nEnter a kind of topping of pizza: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print("we will add " + topping + " to pizza.")    