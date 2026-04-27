
# count, find, index

# count() --------- count presence of given letter 

a="niranjan"
print(len(a))
print(a.count("a"))
print(a.count("z"))


# find() -------- finds index of given letter and gives -1 if not present 

print(a.find('n'))
print(a.find('a'))
print(a.find('r'))
print(a.find('z'))


# index()----------- find index of letter and gives error if not present

print(a.index('n'))
#print(a.index('z')) 


#startswith ---- checks the given character is present or not and give output in true/false

print(a.startswith("n"))
print(a.startswith("z"))
print(a.startswith("ni"))


# endswith

print(a.endswith("n"))
print(a.endswith("jan"))
print(a.endswith("z"))

print("====================================================")

# isalpha() , isnumberic() , isalnum()

name="mahesh@123"

print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

print("====================================================")

# isalpha() , isnumberic() , isalnum()

name="mahesh123"

print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

print("====================================================")

# isalpha() , isnumberic() , isalnum()

name="123"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

print("============================================")

# isspace()

print(" ".isspace())
print(" a".isspace())
print("a ".isspace())

print("============================================")

# istitle()

txt="My Name Is Mahesh"
print(txt.istitle())
 
txt="My name Is Mahesh"
print(txt.istitle())

# join()

arr=["My","name","Is","Mahesh"]
print("@".join(arr))
print("-".join(arr))


# split()
txt="My name Is Mahesh"
arr1=txt.split(" ")
print(arr1)

txt="My-name-Is-Mahe-sh"
arr2=txt.split("-")
print(arr2)

str = "55₹/kg"
arr = str.split("₹")
print(arr)
print(arr[0])


# ljust , rjust -- Left-justifies the string. It adds extra characters on the right side.
# rjust(width, fillchar)
# ljust(width, fillchar)
# center(width, fillchar)

txt="hi"

print(txt.ljust(5,"."))
print(txt.rjust(5,"."))
print(txt.center(6,"."))

print(txt.ljust(5," "))
print(txt.rjust(5," "))
print(txt.center(6," "))

#rstrip , lstrip , strip

txt="     goa      "

print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())


# removeprefix

txt="unhappy"

q1=txt.removeprefix("un")
print(q1)


# removesufficx

str = "55₹/kg"
q2=str.removesuffix("₹/kg")
print(q2)

txt="studentData.txt"
print(txt.removesuffix(".txt"))


# replace()  ---- case sensitive

txt="I love Python programming... python is very rasy to go language..."
q3=txt.replace("Python","Javascript")
print(q3)


# swapcase()
print("MAHESH".swapcase())
print("vishwa".swapcase())
print("VisHWa".swapcase())

# title()
txt = "i love Python programming...python is very easy to go language..."
q3 = txt.replace("Python","Javascript")
print(q3)


# zfill
txt1= "42"
txt2= "788"
print(txt1.zfill(5))
print(txt2.zfill(5))

# partition()

txt3="mahesh_satpute@gmail.com"
x=txt3.partition("@")
print(x)
print(type(x))
x=txt3.partition("@gmail")
print(x)
print(type(x))

# reverse string
name= "mahesh"
rev = name[::-1]
print(rev)