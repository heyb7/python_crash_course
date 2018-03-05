user_names = ['eric', 'john', 'james', 'admin', 'tony']

for name in user_names:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name + ", thank you for logging in again.")