class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.restaurant_name + " servers wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.restaurant_name + " is open. come on in!"
        print("\n" + msg)

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors: ")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand("The Big One", "ice_cream")
big_one.flavors = ["vanilla", "chocolate", "black cherry"]

big_one.describe_restaurant()
big_one.show_flavors()