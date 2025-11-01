# Create a file containing numbers and find the count of all even numbers (total occurance)

# Creating file
with open("/Users/mohit/Documents/py-learning/Practice/I/O/evenCount.txt", 'w') as f:
    f.write("1,2,3,4,5,6,7,8,9") # Created a file

# Reading and finding data
count = 0
with open("/Users/mohit/Documents/py-learning/Practice/I/O/evenCount.txt", 'r') as f:
    data = f.read()
    print(data) # printing the data
    # Basic Code
    # num = '' 
    # for i in range(len(data)):
    #     if(data[i] == ','):
    #         print(int(num)) # casting num into int 
    #         num = ''
    #     else:
    #         num += data[i]

    # Using split() method 
    num = data.split(',')
    for val in num:
        if(int(val) %2 == 0): # casting val into int 
            count += 1

print(count) # Displaying count 