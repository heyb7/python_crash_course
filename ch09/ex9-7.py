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

class Admin(User):
    
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\nThe admin privileges: ")
        for privilege in self.privileges:
            print("- " + privilege)


admin = Admin("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
admin.privileges = ["can add post", "can delete post", "can ban user"]

admin.dcscribe_user()
admin.show_privileges()

