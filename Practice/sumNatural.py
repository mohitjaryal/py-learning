# Write a recursive program to find the sum of first n natural numbers
def fact(n):
    if(n==0 or n==1): # Base comdition
        return 1
    else:
        return fact(n-1) * n
    
print(fact(5))