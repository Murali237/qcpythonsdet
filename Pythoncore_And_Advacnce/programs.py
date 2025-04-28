# Write a program  to read the numbers from keyboard and print sum of two numbers

# num1=eval(input(" enter the first number"))
# num2=eval(input("enter the second number"))
#
# S = num1+num2
# print(S)

#  write a program to read the employee data from keyboard and print that data

# empname=input("enter the name")
# empid=input("enter the emp id")
# empsalary= float(input("enter the emp salary"))
# empdesignation=input("enter the designation")
# empaddress=input("enter the addrress")
#
# print("please confim the emp information")
# print("the employee name is ",empname)
# print("the employee id is  ",empid)
# print("the employee salary is ",empsalary)
# print("the employee desgination is ",empdesignation)
# print("the employee address is ",empaddress)

#  write a program to print the given number is even or odd

# x=12.3
# if x%2==0:
#     print("the given number is even")
# else:
#     print(" the given number is odd")

# wapt find the given number is positive or negative

# x=10
# if x>0:
#  print("the value is positive")
# elif x<0:
#      print("the value is negative")
# else:
#      print("the given number is zero")


# wapt find the given number is prime or not

# num=2
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("the given number is not prime")
#             break
#     else:
#         print(num,"the given number is prime")
# else:
#     print("the given number is not prime")

# num=3
# flag=False
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             flag=True
#             break
#     else:
#          print("the given number is prime")
#
# if flag:
#     print(num,"not a prime number")
# else:
#     print(num,"it is a prime number")

# wapt check the given number is armstrong or not

# x=371
# temp = x
# sum = 0
#
# while temp>0:
#      digit=temp%10
#      sum=sum+digit**3
#      temp=temp//10
#
# if x==sum:
#     print(sum,"the given number is armstrong number")
# else:
#     print(sum,"the given number is not a armstrong")


#  wapt find biggest of two numbers

# x=120
# y=130
# if x>y:
#     print(x," is greater than y")
# else:
#     print(y,"is the bigger number")

# wapt to check whether it is a leap year or not

# year=2000
# if(year%400==0)and(year%100==0):
#     print("it is a leap year")
# elif(year%4==0)and(year%10!=0):
#     print(year,"its a leap year")
# else:
#     print("it is not a leap year")

# wapt print prime numbers b/w given intervals
x=1
y=100
for i in range(x,y):
    if i>1:
        for z in range(2,i):
            if i%z==0:
                break
        else:
            print(i)



