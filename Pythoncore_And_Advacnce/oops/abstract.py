from abc import*
class test():
    @abstractmethod
    def m1(self):
        print(" i am abstract method")

t1=test()
t1.m1()

from abc import*
class act(ABC):
    def m2(self):
        print(" iam abc module")
t2=act()
t2.m2()