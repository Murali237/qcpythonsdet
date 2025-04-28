# class p:
#
#     a=100
#
#     def __init__(self):
#         self.b=200
#
# class j(p):
#
#     c=300
#     def __init__(self):
#         super().__init__()
#         self.d=400
#
# c1=j()
# print(c1.a,c1.b,c1.c,c1.d)


# class parent:
#     a=10
#     def __init__(self):
#         self.b=20
#
#     def m1(self):
#         print("parent class method")
#
#     @classmethod
#     def m2(cls):
#         print("parent class Class method")
#
#     @staticmethod
#     def m3():
#         print("parent class static method")
#
#
# class child(parent):
#     def m1(self):
#         super().m1()
#         print("This is child class instance method")
#
# c=child()
# print(c.a,c.b)
# c.m1()
# c.m2()
# c.m3()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eatdrink(self):
        print("eat biryani and drink beer")

class Employee(person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def work(self):
        print("learing python is very easy")

    def empinfo(self):
        print("employee name :",self.name)
        print("employee age :",self.age)
        print("employee eno :",self.eno)
        print("employee esal :",self.esal)


e=Employee("murali",27,121,2000)
e.eatdrink()
e.work()
e.empinfo()

