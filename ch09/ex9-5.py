class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def dcscribe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nwelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

eric = User("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
eric.dcscribe_user()
eric.greet_user()


print("\nmake 3 times login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("login attempts: " + str(eric.login_attempts))

print("\nreset login attempts...")
eric.reset_login_attempts()
print("login attempts: " + str(eric.login_attempts))