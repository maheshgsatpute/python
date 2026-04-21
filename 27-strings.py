
# strings in python

a="mahesh"
print(a)
print(type(a))

b="""
hello ...
I am learning python
Pyhon is very easy to go language
"""

print(b)
print(type(b))

c='''
hello ...
I am learning python
Pyhon is very easy to go language
"""

print(c)
print(type(c))
'''

# f string in python

fn ="mahesh"
ln ="satpute"

print(f"My name is {fn} and my surname is {ln}")

print("My name is "+fn+" and my surname is "+ln+"...")

print(f"My name is {fn} and \nMy surname is {ln}")

print("My name is "+fn+" and \nMy surname is "+ln+"...")

#===================================================================

#          0         1         2       3
names =["mahesh","vrushali","vishwa","amol"]
print(names[0])
names[0]="satpute"
print(names)


#str is immutable 

name ="mahesh"
print(name[0])
print(name[2])

#name[0]="a"    #TypeError: 'str' object does not support item assignment


#          0         1         2
#          0123   012345   01234567
cities = ["pune","mumbai","banglore"]

print(cities[0])
print(cities[0][0])

print(cities[2][7])

print("banglore" in cities)

name="mahesh"
print("a" in names)
print(len(cities))

# loops 
 
name="mahesh"
print(len(name))

for ch in range(6):
    print(name[ch])

name="mahesh gorksha satpute"
for ch in range(len(name)):
    print(name[ch]) 


print("=====================================")

for ch in name:
    print(ch)

print("========================================")

i=0
while(i<len(name)):
    print(name[i])
    i=i+1

# does substring present in string

a="""
hello ....
I am learning python.
Python is very easy to go language 
"""     

print("python" in a)
print("Python" in a)

print("hello" in a)
print("Hello" in a)

print("am le" in a)

#string method
#upper , lower ,capitlize

x="niRaJan"

print(x.upper())
print(x.lower())
print(x.capitalize())

print(name.capitalize())