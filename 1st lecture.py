print("mahesh")
print(10)
print("10")
print(10+10)
print("10+10")

a=12
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# #100,200
print(100+200)
print(100-200)
print(100*200)
print(100/200)
print(100%200)

#123,4,   234, 6    500, 5   ==>100 pairs===>500
#functions  ==> reusable block of code 

#function without parameter and without return type
#function defination
def calculator():
  print(100+200)
  print(100-200)
  print(100*200)
  print(100/200)
  print(100%200)
  
#call 
calculator()
calculator()

print("----------------------")
#function with parameter and without return type
def calc1(x,y):              #x and y are parameters
  print(x+y)
  print(x-y)
  print(x*y)
  print(x/y)
  print(x%y)

#call 
#      x   y
calc1(200,10)          #200 and 10 are arguments
calc1(123,3)
print("----------------------")
#function with parameter and with return type
# find average of 3 numbers
#function defination
def average(x,y,z):
  res = (x+y+z)/3 
  return res

#call 
avg = average(10,20,30)
print(avg)
print(average(12,34,56))


calculator()