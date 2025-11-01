# WAF to find the first occurance of word 'Java' in practice.txt

def checkWord():
    word = 'java'
    with open('/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt','r') as f:
        data = f.read() # Reading the data
        if(data.find(word) != -1 ):
            print('Found')
        else:
            print("Not found")

# Function to check for the line
def checkline():
     word = 'java'
     data = True
     with open('/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt','r') as f:
         while data: # while data means - do work till data (variable name) has valid data 
             data = f.readline()