 # Basic program to demonstrate the I/O operations in python

f = open('/Users/mohit/Documents/py-learning/I/O_Operations/WriteData/demo.txt','r')

data = f.write("File data is changed ") # overwrites the entire file
print(data)
