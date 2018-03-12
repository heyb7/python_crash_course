from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        return x

die_6 = Die(6)
results = []
for i in range(10):
    result = die_6.roll_die()
    results.append(result)
print("10 rolls of a 6-sides die:")
print(results)


die_10 = Die(10)
results = []
for i in range(10):
    result = die_10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sides die:")
print(results)


die_20 = Die(20)
results = []
for i in range(10):
    result = die_20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sides die:")
print(results)