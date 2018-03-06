sandwich_orders = ['pastrami', 'tuna', 'turkey', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []

print("all out of pastrami today.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")