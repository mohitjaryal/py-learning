# Check if the word 'Hello' exists in the file or not
with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt",'r') as f:
    data = f.read()
    if (data.find('Hello') != -1): # Finding 'Hello'
        print("Found")
    else:
        print("Not found")