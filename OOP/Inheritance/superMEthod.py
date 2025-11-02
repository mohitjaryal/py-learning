# super() method in Python

# Parent class
class Car:
    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        print('Car started')

    @staticmethod
    def stop():
        print('Car stopped')

# Child class
class Toyota(Car):  # Inheriting from Car
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)  # Inheriting properties of the parent class using super() method


t1 = Toyota('Toyota', 'Electric')
t1.start()   # Accessing parent start() method
print(t1.brand)
print(t1.type)
t1.stop()    # Accessing parent stop() method
