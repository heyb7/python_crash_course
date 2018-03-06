
sandwich_orders = ['tuna', 'turkey', 'roast beef']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich")

    finished_sandwiches.append(current_sandwich)

print("\nall of finished sandwich: ")
for sandwich in finished_sandwiches:
    print(sandwich)