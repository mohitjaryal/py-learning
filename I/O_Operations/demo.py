# Basic program to demonstrate the I/O operations in python
f = open("/Users/mohit/Documents/py-learning/I/O_Operations/demo.txt","r")
data = f.read() # Reading the data
print(data) # Printing the data
print(type(data))

f.close() # Closing the file
print("File closed ")