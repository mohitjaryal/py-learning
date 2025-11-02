# Private method in pyhton

class Person:
    # Created a private hello method (we can make any method private by using __)
    def __hello():
        print('Hello') 

p1 = Person()
# print(p1.__hello()) # This will not work because the __hello method is private and can only be call inside the Person class 