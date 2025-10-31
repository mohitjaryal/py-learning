# Find a numbe in tuple
tup = (1,2,3,4,5,6)
user = int(input("Enter the number :"))
found = False
for idx in tup:
    if(idx == user):
        print("Found :",idx)
        found =True
        break
    else:
        print("Not found ")
