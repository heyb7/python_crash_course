pizzas = ["cheese", "beef", "chicken", "mushroom"]

for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizza.")

print("I really love pizza!\n")

friend_pizzas = pizzas[:]

pizzas.append("seafood")
friend_pizzas.append("corn")

print("My favorite pizzas are:")
print(pizzas)

for pizza in pizzas:
    print(pizza)
print("\n")

print("My friend's favorite pizzas are:")
print(friend_pizzas)
for pizza in friend_pizzas:
    print(pizza)