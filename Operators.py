# Operators 
# Operators are of 2 types : Arithmetic and Logical Operators
# Arithmetic Operators include Addition(+), Subtraction(-), Multiplication(*), Division(/), Quotient(//), Remainder(%)
# Logical Operators include AND, OR, XOR, NOT etc.

# Type keyword is used to check the type of data that we are dealing with

## Arithmetic Operations:
x = int(input("Enter The first number: "))
y = int(input("Enter The second number: "))

print(type(x), type((y)))

# Addition
print("Addition output is : ", x+y)
print("Subtraction output is : ", x-y)
print("Multiplication output is : ", x*y)
print("Dicision output is : ", x/y)
print("Quotient output is : ", x//y)
print("Remainder output is : ", x%y)
print("\n")


str1 = input("Enter first word : ")
str2 = input("Enter second word : ")

# strings only supports addition and multiplication operation 
print("String addition result is : ", str1+str2)

print("String multiplication result is : ", str1*3)

# For comparison operators output is Boolean data type
# Boolean data type has two types of output : True, False
# Comparison operators examples are : >, <, >=, <=, ==

test1 = 23
test2 = 36

print(test1 > test2)
print(test1 < test2)
print(test1 >= test2)
print(test1 <= test2)
print(test1 == test2)
print(test1 != test2)
