class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.restaurant_name + " servers wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.restaurant_name + " is open. come on in!"
        print("\n" + msg)

mean_queen = Restaurant("the mean queen", "pizza")
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", "seafood")
ludvigs.describe_restaurant()

mango_thai = Restaurant("mango thai", "thai food")
mango_thai.describe_restaurant()