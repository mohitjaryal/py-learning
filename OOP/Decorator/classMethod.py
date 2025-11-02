# @classmethod in py

class Parent:
    name = 'Abc'


    @classmethod # decorator
    def changeName(cls,name):
        cls.name = name

p1 = Parent() # Object
print('Before :',p1.name)
p1.changeName('Mohit')
print('After :',p1.name)
print('After :',p1.name)