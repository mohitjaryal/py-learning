# Create a student class that takes name & marks of 3 subjects as argument in constructor then create a method & print 

# Student class

class Student:
    # Constructor
    def __init__(self,name,marks):
       self.name = name
       self.marks = marks

    # Method

s1 = Student('Mohit',[98,99,100])