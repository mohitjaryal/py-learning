# Program to find the average of 3 no.
def avg(a,b,c):
    sum = a + b + c
    ans = sum / 3
    print(ans)
    return ans

a= int(input("Enter 1st no. :"))
b = int(input("Enter 2nd no. :"))
c = int(input("Enter 3rd no. :"))

avg(a,b,c)