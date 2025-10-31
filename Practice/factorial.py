# WAP to find factorial of n no. using for loop
inp = int(input("Enter the no. :"))
fact = 1
for i in range(1,inp+1):
    fact*= i
print("Factorial is :",fact)   