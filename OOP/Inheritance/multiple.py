# Multiple inheritance

class Parent1:
    hello = 'Hello from parent 1'

class Parent2:
    hello = 'Hello from parent 2'

class Child(Parent1,Parent2):
    hello = 'Hello form Child'

c1 = Child() # Object of Child class
