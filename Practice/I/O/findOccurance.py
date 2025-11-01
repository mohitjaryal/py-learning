def checkWord():
    word = 'Java'
    with open('/Users/mohit/Documents/py-learning/Practice/I/O/findOccurance.txt','r') as f:
        data = f.read() # Reading the data
        if(word in data):
            print('Word Found\n')
        else:
            print("Not found")

# Function to check for the line
def checkline():
    word = 'Java'
    data = True 
    lineNo = 1 # line no.
    with open('/Users/mohit/Documents/py-learning/Practice/I/O/findOccurance.txt','r') as f:
        while data: # while data means - do work till data (variable name) has valid data 
            data = f.readline()
            if(word in data):
                print('Found at line :',lineNo)
                return  # stop after finding the first occurrence
            lineNo += 1  # updating line no.
    return -1 # if the word doesn't exist 

checkWord() # function call
checkline() # function call