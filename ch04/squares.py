squares1 = []
for value in range(1, 11):
    square = value ** 2
    squares1.append(square)

print(squares1)

squares2 = [value**2 for value in range(1,11)]
print(squares2)