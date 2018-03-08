def make_sandwich(*toppings):
    print("\nI will make a sandwich:")
    for topping in toppings:
        print(" -add " + topping + " to the sandwich.")
    print("the sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')