# Check value in tuple using loop
tup = (1,2,3,5,6,7,8574,6,436,234,5,65,7,36,36,3624,7,57,87)
user = int(input("Enter the value you want to check: "))
idx = 0
found = False

while idx < len(tup):
    if user == tup[idx]:
        print('Found at index:', idx)
        found = True
    idx += 1

if not found:
    print('Not found')