# WAP to create a file using py and write data in it

with open("/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt",'w') as f: # w mode - creating new file
    f.write("I have created a new file !") # Writing this message to the new file 
    f.write("Python!")
    f.write("Java")
    f.write("JavaScript")
    f.write("React")