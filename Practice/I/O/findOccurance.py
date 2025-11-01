# WAF to find the first occurance of word 'Java' in practice.txt

def checkWord();
    word = 'java'
    with open('/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt','r') as f:
        data = f.read() # Reading the data
        if(data.find(word) != -1 ):
            print('Found')
        else:
            print("Not found")