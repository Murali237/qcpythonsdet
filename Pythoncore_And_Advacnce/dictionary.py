# creating empty dictionary

d={}
print(d)
print(type(d))

# another way of creating dictionary
d1=dict()
print(d1)
print(type(d1))

# add objects to dict

d[100]="murali"
d[200]="goud"
d[300]="panjala"
print(d)
print(d[100])

# write a program to enter the name and percentage of marks in dict and display information

# x={}
# n=int(input("enter the number of students"))
# i=1
# while i<=n:
#     name = input("enter the name of the student")
#     marks = input("enter the percentage of marks")
#     x[name]=marks
#     i=i+1
#
# print(x)
# print("\t\t","name of the student","\t\t","% of marks")
# for z in x:
#     print("\t\t",z,"   \t\t",x[z])

# d.clear()
# print(d)

#  to get the keys of dict
print(d.keys())

#  to get values for the particular key
print(d.get(200))

# 
