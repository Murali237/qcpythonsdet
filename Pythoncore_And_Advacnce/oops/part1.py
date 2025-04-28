# import sys
#
#
# class customer:
#    """customer class with bank details"""
#    bankname="QAcirclabank"
#
#
#    def __init__(self,name,balance=0.0):
#        self.name=name
#        self.balance=balance
#
#    def deposit(self,amt):
#        self.balance=self.balance+amt
#        print("balance after deposit :",self.balance)
#
#    def withdraw(self,amt):
#        if amt>self.balance:
#            print("insufficient funds muskonii kurchoo ra puvulla chokka ")
#            sys.exit()
#        self.balance=self.balance-amt
#        print("balance after withdraw :", self.balance)
#
#    def enquiry(self,amt):
#        self.balance=self.balance
#        print("your account as no funds",self.balance)
#
# print("welcome to ",customer.bankname)
# name=input("enter the name")
# c=customer(name)
# c.deposit(10000)
# c.withdraw(2500)
# c.deposit(10000)
#
# while True:
#     print("d-deposit\nw-withdraw\ne-Exit")
#     option=input("choose your option")
#     if option=='d' or option=='D':
#         amt=float(input("enter the amount"))
#         c.deposit(amt)
#     elif option=='w' or option=='W':
#         amt=float(input("enter the amount"))
#         c.withdraw(amt)
#     elif option=='e' or option=='E':
#         print("thank you for banking with us")
#         sys.exit()
#     else:
#         print("please enter the valid input")

# wapt count no of objects created

# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1
#
#     @classmethod
#     def noofobjects(cls):
#         print("the number of objects created are:",cls.count)
#
#
# t1=Test()
# t2=Test()
# Test.noofobjects()
# t3=Test()
# t4=Test()
# Test.noofobjects()

# set and get method

class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
n=int(input("enter the no of students"))
for i in range(n):
    s=student()
    name=input("enter the name")
    s.setname(name)
    marks=input("enter the marks")
    s.setmarks(marks)

    print("hi my name is :",s.getname())
    print("my marks are :", s.getmarks())