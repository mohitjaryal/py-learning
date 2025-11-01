# Form a file containing numbers and find the count of all even numbers
# Creating file
with open("/Users/mohit/Documents/py-learning/Practice/I/O/evenCount.txt", 'w') as f:
    f.write("1,2,3,4,5,6,7,8,9") # Created a file

# Reading and finding data
with open("/Users/mohit/Documents/py-learning/Practice/I/O/evenCount.txt", 'r') as f:
    data = f.read()
    print(data) # printing the data
    