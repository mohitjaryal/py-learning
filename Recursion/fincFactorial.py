# Write a recursive function to calculate the factorial 
def fac(n):
    if(n == 0 or n == 1): # Base case
        return 1
    else:
        return n * fac(n-1) # Final argument
    
print(fac(5))