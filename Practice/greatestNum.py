# WAP to find the greatest among 3 numbers entered by user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2 and num1 >= num3):
    print(num1, "is greatest")
elif (num2 >= num1 and num2 >= num3):
    print(num2, "is greatest")
elif (num3 >= num1 and num3 >= num2):
    print(num3, "is greatest")
else:
    print("Gadbad ho gye bhai")
