# Basic demonstration of inheritance 

# Parent class
class Car:
    @staticmethod
    def start():
        print('Car started')

    @staticmethod
    def stop():
        print('Car stopped')

# Child class
class Toyota(Car):  # ✅ Inheriting from Car
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


t1 = Toyota('Toyota', 'Fortuner')
t1.start()   #  Accessing parent start() method
print(t1.brand)
print(t1.model)
t1.stop()    # Accessing parent stop() method
