# WAP to create a file using py and write data in it

with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt",'+w') as f:
    f.write("I have created a ne file !")
    data = f.read()
    print(data)