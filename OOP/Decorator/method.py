# Simple demonstration of methods in python

# Creating class
class Student:
    def __init__(self,fullName):
        self.name = fullName

    # Creating method
    def hello(self):
        print('Hello',self.name)

# Object (Instance)

s1 = Student('Mohit')
s1.hello()