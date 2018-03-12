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

restaurant = Restaurant("the mean queen", "pizza")
print("Number served: " + str(restaurant.number_served) + ".")

restaurant.number_served = 200
print("\nNumber served: " + str(restaurant.number_served) + ".")

restaurant.set_number_served(300)
print("\nNumber served: " + str(restaurant.number_served) + ".")

restaurant.increment_number_served(20)
print("\nNumber served: " + str(restaurant.number_served) + ".")