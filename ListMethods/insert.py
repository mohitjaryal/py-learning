# insert() method in py
num = [1,2,3,4,6]
print("Before inserting",num)
idx = int(input("Enter the index number :"))
val = input("Enter the value :")

newIdx = num[:idx] + [val] + num[idx:] # adding new value to the desired index
print("After inserting :",newIdx)