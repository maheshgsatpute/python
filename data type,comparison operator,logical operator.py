a=10
print(a)
print(type(a))

a=10.5
print(a)
print(type(a))

a="dipanshu@123"
print(a)
print(type(a))

a="10+10"
print(a)
print(type(a))

a=False
print(a)
print(type(a))

true=100
a=true
print(a)
print(type(a))


#comparison operator
#==,!=,>,>=,<,<=

print(3==3)
print(3!=3)
print(4>4)
print(4<2)
print(4<=2)
print(4<=5)

print("=========================")

#logical operator(and,or,not)

#and==> if any of inputs is false then output is false, true only when all inputes are true

#ip   ip     op
#T    T      T
#T    F      F
#F    T      F
#F    F      F

print(3==3 and 3!=4)
print(3==3 and 3>4)
print(3!=3 and 3>2)
print(3!=3 and 3>4)
print("================================")

#or==> if any of input is true then output is true, false only when all the inputs are false
 
#T   T =  T
#T   F =  T
#F   T =  T
#F   F =  F  
print(4>2 or 4<5)
print(4>2 or 4<3)
print(4==5 or 4>2)
print(4==5 or 4>6)
print("=============================")

#not
#true==> false
#false==> true
print(not(3==3))

#not T==> F

print(not(3>6))

print(not(3==3 and 3>4))

#not(t and f)
#not f==> t)
print(not(3==3 or 3>4))

#not (t ot f)
#not(t)==> f
