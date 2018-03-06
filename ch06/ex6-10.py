favorite_numbers = {
    'lily': [10, 20, 30, 40],
    'james': [13, 23, 33, 43],
    'tony': [11, 21, 31, 41],
    'john': [22, 30, 50],
    'eric': [18, 28, 38],
}

for name, numbers in favorite_numbers.items():
    print('\n' + name + "'s favorite number:")
    for num in numbers:
        print('\t' + str(num))