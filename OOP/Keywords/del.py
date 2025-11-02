# del keyword in pyhton
class Student:
    def __init__(self,name):
        self.name = name 

s1 = Student('Mohit')
print(s1.name)
del s1.name # deleting s1.name attribute
# del s1 # delting s1 object 
print(s1)