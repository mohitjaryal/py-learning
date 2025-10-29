# WAP to find the greatest amon 3 numbers entered by user
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if(num1 > num2 and num2 < num3):
    print(num3,'is greates')
elif(num3 > num2 and num3 > num1):
    print(num3,'is greatest')
else:
    print("Gadbad ho gye bhai")