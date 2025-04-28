# list=[100,200,True,False,"Murali","Car","Bike"]
# len(list)
# print(list[::-1])
# print(list[1:2:3])
# print(list[-1::])
# list.append(242)
# print(list)


# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1
#
# for x in list:
#     print(x)

# l=[2,4,6,5,8,7,9,4,2,1,3,0,4,2,4]
# for x in l:
#     if x%2==0:
#         print(x,end=' ')
# print()
#
# l1=["a","b","c"]
# z=len(l1)
# for i in range(z):
#     print(l1[i],"the positive index is presented at :",i,"and the nagative undex is presnted at :",i-z)
# print(l.count(4))
#
# print(l.index(2))

# write a program to add elements upto 100 which are divisble by 9
#
# list1=[]
# for i in range(100):
#     if i%9==0:
#         list1.append(i)
# print(list1)

# l=[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
# l.insert(2,143)
# print(l)
#
# # extend()
#
# order1=["egg","white","sweet potatoo","spourts","lemon tea"]
# order2=["chicken","rice","curd","green tea"]
# print(id(order1)," ",id(order2))
# print(order1)
# order1.extend(order2)
# print(order1)
# l=order1+order2
# print(l)

# pop()
# print(order1.pop())
# print(order1)

# reverse()

 # l=[10, 32, 80, 50, 70, 90, 40, 5, 6, 68]
# print(l)
# l.reverse()
# print(l)

# sorting
# l=[90,80,70,60,10,20,30,40,50]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)

#
# s=[x*x for x in range(100)]
# print(s)
# print(type(s))
# words=["murali","goud","panjala"]
# l=[w[0] for w in words]
# print(l)

vowels=['a','e','i','o','u']
name='muraligoudpanjala'
l=[i for i in name if i in vowels]
print(l)

