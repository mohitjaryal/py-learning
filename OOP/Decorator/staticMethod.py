# @ststicmethod decorator in py

# Creating class
class Student:
    def __init__(self,fullName):
        self.name = fullName

    # Creating method
    def hello(self):
        print('Hello',self.name)
    
    # Static method
    @staticmethod
    def bye():
        print('Bye')
# Object (Instance)

s1 = Student('Mohit')
s1.hello()
s1.bye()