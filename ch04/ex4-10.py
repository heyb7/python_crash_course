cubes = []

for value in range(1, 11):
    cubes.append(value**3)

#for value in cubes:
#    print(value)

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[2:5])

print("The last three items in the list are:")
print(cubes[-3:])