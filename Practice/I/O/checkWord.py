# Check if the word 'Python' exists in the file or not
with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt", 'r') as f:
    data = f.read()
    if 'Python' in data:
        print("Found Python :\n")
    else:
        print("Not found")