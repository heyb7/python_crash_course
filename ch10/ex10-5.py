filename = "programming_poll.txt"

print("Enter 'quit' to end the programm.")

while True:
    msg = input("why do you like programming? ")
    if msg == 'quit':
        break
    else:
        with open(filename, "w") as f:
            f.write(msg)