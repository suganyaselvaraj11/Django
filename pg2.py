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
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age > 20:
        print("u r eligible")
    else:
        print("Hello " + name + " your age is " + str(age))
        print("u r not eligible")
    myname(name, age)
