cars1 = ["bmw", "audi", "toyota", "subaru"]
print(cars1)
cars1.sort()
print(cars1)

cars1.sort(reverse=True)
print(cars1)

cars2 = ["bmw", "audi", "toyota", "subaru"]
print("\nHere is the original list:")
print(cars2)
print("\nHere is the sorted list:")
print(sorted(cars2))
print("\nHere is the original list again:")
print(cars2)

print("\n")

cars3 = ["bmw", "audi", "toyota", "subaru"]
print(cars3)
cars3.reverse()
print(cars3)
print("length of the cars list is: ", len(cars3))