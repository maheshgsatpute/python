#conditional operators
#if, elif, else
#to get multiple outputs from one input

#num 0 to 5 it gets 5% discount ==> 6 to 10 get 10% discount ==> above 10 get 20% discount 

num=2
if num>0 and num<=5:
    print("5% discount")
if num>5 and num<=10:
    print("10% discount")
if num>10:
    print("20% discount")         
    
#=========================================================

num=-2
if num>0 and num<=5:
    print("5% discount")
elif num>5 and num<=10:
    print("10% discount")
elif num>10:
    print("20% discount")
else:
    print("invalid input")                


print("=====================================================")
# marks >90 get A grade , >75 B grade ,>65 C grade
marks=95
if marks>90:
    print("A")
if marks>75:
    print("B")
if marks>65:
    print("C")
            

marks=30
if marks>90:
    print("A")
if marks>75:
    print("B")
if marks>65:
    print("C")         
#in above line of code not get any output becuse not any condition match to the marks 

if marks>90:
    print("A")
elif marks>75:
    print("B")
elif marks>65:
    print("C")
else:
    print("please try again")            
    print("=================================================")


marks=66

if marks>90:
    print("A")
elif marks>75:
    print("B")
elif marks>65:
    print("C")
    print("=================================")

#bigger number from 2 given number
a=100
b=200
if a>b:
    print("a is bigger")
elif b>a:
    print("b is bigger")
else:
    print("both are equal")            

#bigger number from 3 given number 
x=100
y=200
z=300

if x>y and x>z:
    print("x is bigger")
elif y>x and y>z:
    print("y is bigger")
elif z>x and z>y:
    print("z is bigger")

#=================================================

x=100
y=200
z=200

if x>y and x>z:
    print("x is bigger")
elif y>x and y>z:
    print("y is bigger") 
elif z>x and z>y:
    print("z is bigger")
else:
    print("either all or bigger two number are equal")           