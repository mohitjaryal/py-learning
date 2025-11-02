# Multiple inheritance

class Parent1:
    hello1 = 'Hello from parent 1'

class Parent2:
    hello2 = 'Hello from parent 2'

class Child(Parent1,Parent2):
    hello3 = 'Hello form Child'

c1 = Child() # Object of Child class
print(c1.hello1)# Inherited from parent1
print(c1.hello2) 
print(c1.hello3) 