print("Welcome to the Calculator Program!")

question = input("What operation do you want to use \n1. Addition + \n2. Subtraction - \n3. Multiplication x \n4. Division / \n5. Quotient // \n6. Remainder % \n Choose any : ")

num1 = int(input("Choose you First Number: "))

num2 = int(input("Choose you Second Number: "))

if question == "1":
    total = num1 + num2
    print("The sum of {} and {} is {}".format(num1, num2, total))

elif question == "2":
    total = num1 - num2
    print("The difference of {} and {} is {}".format(num1, num2, total))

elif question == "3":
    total = num1 * num2
    print("The product of {} and {} is {}".format(num1, num2, total))

elif question == "4":
    total = num1 / num2
    print("The division of {} and {} is {}".format(num1, num2, total))

elif question == "5":
    total = num1 // num2
    print("The quotient of {} and {} is {}".format(num1, num2, total))

elif question == "6":
    total = num1 % num2
    print("The remainder of {} and {} is {}".format(num1, num2, total))

elif question == "7":
    total = (num1 ** num2)
    print("The power of {} and {} is {}".format(num1, num2, total))

else:
    print("The Number You Have written is Invalid")