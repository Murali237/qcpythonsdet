class Employee:

    # constructor for initialization
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # instance method
    def emp_data(self):
        print("name of the employee :",self.name)
        print("age of the employee :",self.age)

class data:

    def __init__(self,address,salary,emp_obj):
        self.address=address
        self.salary=salary

        # creating object of Employee class
        self.emp_obj = emp_obj

    # instance method
    def display(self):

        # calling Employee class emp_data()
        # method
        self.emp_obj.emp_data()
        print("Address of the employee :",self.address)
        print("salary of the employee :",self.salary)

# creating employee class object
emp=Employee("murali",27)

# passing obj. of Emp. class during creation
# of data class object

Data=data("bibinagar",20000,emp)

Data.display()