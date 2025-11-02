# Define an Employee class with attributes role, department & salary. This class also a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

# Employee class (parent)
class Employee:

    # Constructor
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    # showDetail() method
    def showDetail(self):
        print('Role :',self.role)
        print('Departent :',self.dept)
        print('Salary :',self.salary)

 # Engineer class (child)
  
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__('Engineer','IT','1,00,000,00')

eng1 = Engineer('Elon Musk ',55)
eng1.showDetail()