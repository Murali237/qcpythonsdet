# t=10,20,30
# print(t)
# print(type(t))
#
# T=()
# print(type(T))
#
#  mathematical operation
# t1=(10,20,30)
# t2=(40,50,60)
# t3=(t1+t2)
# print(t3)
# t4=t1*2
# print(t4)
# r=(60,70,30,50,40,10,20)
# r1=sorted(r)
# print(r1)
# r2=sorted(r1,reverse=True)
# print(r2)
# print(min(r2))
# print(max(r2))
from pycparser.ply.cpp import t_CPP_COMMENT2

# tuple packing
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)
print(type(t))

# tuple unpacking

w,x,y,z=t
print(w,x,y,z)