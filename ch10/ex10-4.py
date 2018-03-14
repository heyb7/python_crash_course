filename = "guest_book.txt"

print("Enter 'quit' to end the programm.")

while True:
    name = input("Enter you name: ")
    if name == 'quit':
        break
    else:
        msg = "Welcome to back, " + name
        print(msg)
        with open(filename, "w") as f:
            f.write(msg)

    