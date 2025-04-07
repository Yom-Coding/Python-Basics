num = int(input("Enter a number: "))
temp = num 
rev = 0

while temp > 0:
    dig = temp % 10
    rev = (rev * 10) + dig
    temp = temp//10

if num == rev:
    print("Your Number Is Palindrome")

else:
    print("Your Number Is not Palindrome")



