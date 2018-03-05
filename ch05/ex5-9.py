#user_names = ['eric', 'john', 'james', 'admin', 'tony']
user_names = []

if user_names:
    for name in user_names:
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + name + ", thank you for logging in again.")
else:
    print("We need to find some users!")