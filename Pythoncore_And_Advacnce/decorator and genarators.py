def decor(func):
    def inner(name):
        if name=="murali":
            print("hello murali gd mrng")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("hello",name,"hi how r u")

wish("murali")
wish("harish")

print("************")
# how to call the same function with and without decarator

def decor(func):
    def inner(name):
        if name=="murali":
            print("hello murali gd mrng")
        else:
            func(name)
    return inner

modify=decor(wish)
modify("murali")
modify("harish")

# ex 3
def make_pretty(func):
    def inner():
        print(" i got decarator")
        func()
    return inner

@make_pretty
def ordinary():
    print("i am ordinary")

ordinary()

#  smart division ith decarator function
def smart_divide(func):
    def inner(a,b):
        print(" i am going to divide",a, "and", b)
        if b==0:
            print("oops cant divide")
            return
        return func(a,b)
    return inner
@ smart_divide
def divide(a,b):
    print(a/b)

divide(10,2)
divide(2,0)

#  decorator chaining

def printer(msg):
    print(msg)

printer("hello")
