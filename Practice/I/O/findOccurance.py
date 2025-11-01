def checkWord():
    word = 'java'
    with open('/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt', 'r') as f:
        data = f.read()
        if word.lower() in data.lower():
            print('Found')
        else:
            print("Not found")


def checkLine():
    word = 'java'
    lineNo = 1
    with open('/Users/mohit/Documents/py-learning/Practice/I/O/practice.txt', 'r') as f:
        for line in f:
            if word.lower() in line.lower():
                print(f"Found on line {lineNo}")
                return lineNo   # stop after first occurrence
            lineNo += 1
    print("Not found")
    return -1  # if the word doesn't exist


# Function calls
checkWord()
checkLine()
