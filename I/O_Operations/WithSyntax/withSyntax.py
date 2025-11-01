# with syntax in py to perform i/o operations
 
# with syntax
with open("/Users/mohit/Documents/py-learning/I/O_Operations/WithSyntax/demo.txt","r") as f:
    data = f.read()
    print(data)
    f.close() # Closing file