current_users = ['lily', 'xiaoming', 'james', 'tony', 'John']

new_users = ['antony', 'paul', 'booker', 'james', 'JOHN']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", the name is taken.")
    else:
        print("Great, " + new_user + " is still available.")