# WAP to check whether the entered number is even or odd
num =int(input("Enter the number :"))
if(num % 2 == 0):
    print(num,"is an even number ")
elif(num % 2 != 0):
    print(num,"is an odd number")
else:
    print("Error occur ! Try again")