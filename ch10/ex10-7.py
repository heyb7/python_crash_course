print("Please enter two numbers.")
print("Enter 'q' to quit.")

while True:
    try:
        first_num = input("first number: ")
        if first_num == 'q':
            break
        first_num = int(first_num)

        second_num = input("second number: ")
        if second_num == 'q':
            break
        second_num = int(second_num)

    except ValueError:
        print("Sorry, I need a number.")
    else:
        sum = first_num + second_num
        print("The sum of " + str(first_num) + " and " + str(second_num) + " is " + str(sum) + ".")