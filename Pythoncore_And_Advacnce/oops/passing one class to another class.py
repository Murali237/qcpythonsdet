class Employee:

    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print("The employee number is :",self.eno)
        print("The employee name is :", self.ename)
        print("The employee salary is :", self.esal)



class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()


e = Employee(121, "murali", 20000)
Test.modify(e)


# wapt check how many no of reference variables are created for object

