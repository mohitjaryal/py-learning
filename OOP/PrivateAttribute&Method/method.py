# Private method in pyhton

class Person:
    # Created a private hello method (we can make any method private by using __)
    def __hello(self):
        print('Hello') 

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome()) # Calling hello() method 
# print(p1.__hello()) # This will not work because the __hello method is private and can only be call inside the Person class 