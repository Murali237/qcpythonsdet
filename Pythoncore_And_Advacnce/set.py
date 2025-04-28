s={10,20}
print(s)
print(type(s))

s1=set()
print(type(s1))

l=[10,20,30]
s2=set(l)
print(s2)
print(type(s2))

l1=[10,20,30,40]
s.update(range(44,51))
print(s)

r=set("murali")
print(r)
print('m' in r)
print('k' in r)

# to eliminate the duplicate element in list

l={"aq","bg","ge","aq",10,20,10,20}
s4=set(l)
print(s4)

l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

vowels={'a','i','e','o','u'}
name="muraligoudpanjalafrombibinagar"

l2=[]
for m in name:
    if m in vowels and m not in l2:
        l2.append(m)
print(l2)



