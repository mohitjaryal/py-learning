# Private attribute in py
class Account:
    def __init__(self,acc,userName):
        self.__acc_no = acc # created a private acc_no attribute
        self.userName = userName

acc1 = Account('12345','Mohit')

# print(acc1.__acc_no) # this will not print because acc_no is private attribute
print(acc1.userName)