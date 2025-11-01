# Check if the word 'Hello' exists in the file or not
with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt", 'r') as f:
    data = f.read()
    if 'Hello' in data:
        print("Found")
    else:
        print("Not found")
