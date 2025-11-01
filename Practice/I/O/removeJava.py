# WAF tp remove java from practice.txt 
# Reading data
with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt", 'r') as f:
    data = f.read() # Reading the file
    print("Old data :\n",data)

newData = data.replace("Java","HTML")
print(newData) # Displaying newData
f.close() # Closing the file
