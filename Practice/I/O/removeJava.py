# WAF tp remove java from practice.txt 
# Reading data
with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt", 'r') as f:
    data = f.read() # Reading the file

newData = data.replace("Java","")
print(newData) # Displaying newData
f.close() # Closing the file
