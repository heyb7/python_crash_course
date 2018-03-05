favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = ['jen', 'eric', 'nil', 'tony', 'phil']

for user in users:
    if user in favorite_languages.keys():
        print("Thank you for taking the poll, " + user.title() + "!")
    else:
        print(user.title() + ", what's your favorite programming language?")