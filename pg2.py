"""
def myprog(x,y):
    if(x>y):
        print("x is bigger")
    elif(x == y):
        print("both are same")
    else:
        print("y is bigger")
myprog(x=10,y=15)
myprog(10,6)
"""
def myname(name, age):
    print("Hello " + name + " your age is " + str(age))

name = input("Enter your name: ")
age = input("Enter your age: ")

myname(name, age)
