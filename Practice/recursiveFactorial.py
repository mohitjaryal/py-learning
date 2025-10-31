# Write a recursive program to find factorial using recursion

def fact(n):
    if(n==0 or n==1): # Base comdition
        return 1
    else:
        return fact(n-1) * n
    


n = int(input("Enter the number :"))
if(n < 0):
    print("Invalid input !")
else:
   print("Factorial of", n, "is:", fact(n))