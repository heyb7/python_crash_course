filename = "guest.txt"

name = input("Enter you name: ")

with open(filename, "w") as f:
    f.write(name)