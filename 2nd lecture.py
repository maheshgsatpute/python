print("dipanshu")
print(10)
print(10+10)
print("10+10")
#functions
#+,-,*,/,%
#function without parameter and without return type
def calculator():
  print(100+200)
  print(100-200)
  print(100*200)
  print(100/200)
  print(100%200)

calculator()
calculator()
print("----------------------------")
#-----------------------------------
x=10
y=20
def calc1(x,y):
 print(x+y)
 print(x-y)
print(x*y)
print(x/y)
print(x%y) 

print("-------------------------------")
calc1(123,2)

def calc1(x,y):
  print(x+y)
  print(x-y)
  print(x*y)
  print(x/y)
  print(x%y)
print("--------------------------")
calc1(123,2)
calc1(222,2)
print("--------------------------")

#function with parameter and return type

def average(x,y,z):
  result=(x+y+z)/3
  return result
avg=average(10,20,30)
print(avg)

#function with return type and parameter
#balance deposit,withdraw 
balance=10000

def deposit(amount):
  return balance+amount

def withdraw(amount):
  return balance-amount

print(balance)
balance=withdraw(5000)
print(balance)

balance=deposit(7000)
print(balance)
  



