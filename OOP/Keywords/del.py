# del keyword in pyhton
class Student:
    def __init__(self,name):
        self.name = name 

s1 = Student('Mohit')
print(s1.name)
del s1.name
print(s1)