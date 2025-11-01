# WAP to create a file using py and write data in it

# Writing
with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt", 'w') as f:
    f.write("I have created a new file!\n")
    f.write("Python!\n")
    f.write("Java\n")
    f.write("JavaScript\n")
    f.write("React\n")
    f.close()

# Reading back to confirm
with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt", 'r') as f:
    print(f.read())
    f.close()
