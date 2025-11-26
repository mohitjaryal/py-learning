# Basic program to demonstrate the read() operation in python
f = open("/Users/mohit/Documents/py-learning/I/O_Operations/demo.txt","r")

data = f.read() # Reading the data - entire data
# data = f.read(5) # Reading first 5 letter or char 
print(data) # Printing the data
print(type(data))

f.close() # Closing the file
print("File closed ")