
info = {
    "name" : "mahesh" ,
    "age" : 30 ,
    "location" : "pune"
}

print(info)

students = info 
print(students)

students["surname"] = "satpute"
print(students)

#==================================================

students2 = info.copy()
print(info)
print(students2)

students2["skills"] = "python"
print(students2)

print(info)