# Create a class called Order which stores items & it's price
# Use dunder function __gt__() to convey that:
#   order1 > order2 if price of order1 > order2

class Order:

    # Constructor
    def __init__(self,items,price):
        self.items = items
        self.price = price

    # Dunder function
    def __gt__(self,odr2):
        return self.price > odr2.price


odr1 = Order('Pizza',200)
odr2 = Order('Burger',80)
print('Item1 :',odr1.items,'Price :',odr1.price)
print('Item2',odr2.items,'Price :',odr2.price)
print(odr1 > odr2)