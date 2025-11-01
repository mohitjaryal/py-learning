# Create a student class that takes name & marks of 3 subjects as argument in constructor then create a method to find average & print

# Student class
class Student:
    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to calculate average
    def avg(self):
        total = 0
        for val in self.marks:
            total += val
        print('Hi', self.name, 'your average score is:', total / 3)


# Creating object
s1 = Student('Mohit', [98, 99, 100])

# Calling method
s1.avg()
