filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        #print("sorry, file " + filename + " is not find.")
        pass
    else:
        print("\nread file: " + filename)
        print(contents)