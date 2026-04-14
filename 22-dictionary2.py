
# CRUD in dict

info = {
    "name" : "virat" ,
    "surname" : "koholi" ,
    "age" : 35 ,
    "city" : "mumbai" 
}

#retrive
print(info)

a=info.get("name")
print(a)

b=info.get("city")
print(b)

# delete

# delete all items

info.clear()
print(info)

# pop()

info = {
    "name" : "virat" ,
    "surname" : "koholi" ,
    "age" : 35 ,
    "city" : "mumbai" 
}

info.pop("age")
print(info)

# info.pop("location")       # keyErrror : "location"

info.pop("location" , None)

#popitem : delete last key

print(info)
info.popitem()
print(info)

#del : delete key from dictionary

del info["name"]
print(info)

info = {
    "name" : "virat" ,
    "surname" : "koholi" ,
    "age" : 35 ,
    "city" : "mumbai" 
}

print(info)
info.update({"team" : "mumbai indians "})
print(info)

info.update({"team" : "RR"})
print(info)

info["color"] = "blue"
print(info)

info["color"] = "sky blue"
print(info)

info.setdefault("batch" , "2029")
print(info)


info = {
    "name" : "virat" ,
    "surname" : "koholi" ,
    "age" : 35 ,
    "city" : "mumbai" 
}

info.setdefault("city" , "pune")
print(info)

info.update({"city" : "pune"})
print(info)