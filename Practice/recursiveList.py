# Recursive function to print a list

def rec(name, idx):
    if idx == len(name):      # base case: stop when index reaches end
        return
    else:
        print(name[idx])      # print current element
        rec(name, idx + 1)    # recursive call for next index

# List
name = ['Mohit', 'Rohit', 'Raj']

# Function call starting from index 0
rec(name, 0)
