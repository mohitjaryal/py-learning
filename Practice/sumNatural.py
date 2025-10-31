# Write a recursive program to find the sum of first n natural numbers using recursion

def sum(n):
    if(n == 0): # Base case
        return 0
    else:
        return n + sum(n - 1)

n = int(input("Enter the number :"))

print("Sum :",sum(n))