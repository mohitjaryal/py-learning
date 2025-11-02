# del keyword in pyhton
class Student:
    def __init__(self,name):
        self.name = name 
        print(name)

s1 = Student('Mohit')

del s1.name
print(s1)