def make_pizza(*toppings):
    #print(toppings)
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


def make_pizza_1(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_1(16, "pepperoni")
make_pizza_1(12, "mushrooms", "green peppers", "extra cheese")