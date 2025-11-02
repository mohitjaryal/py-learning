# Private attribute in py
class Account:
    def __init__(self,acc,userName):
        self.__acc_no = acc
        self.userName = userName