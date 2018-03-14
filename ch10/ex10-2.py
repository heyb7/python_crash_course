filename = "learning_python.txt"

with open(filename) as f:
    for line in f:
        msg = line.replace("Python", "C")
        print(msg)