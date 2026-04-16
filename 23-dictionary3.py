
info = {
    "fname" : "virat" ,
    "lname" : "kohli",
    "age" : 38 ,
    "city" : "mumbai"
}

a=info.get("fname")
print(a)

b=info.get("city")
print(b)

info.clear()
print(info)



info = {
    "fname" : "virat" ,
    "lname" : "kohli",
    "age" : 38 ,
    "city" : "mumbai"
}

info.popitem()              # popitem removes the last element
print(info)

info.pop("agee" , None)
print(info)

# ====================================================


info = {
    "fname" : "virat" ,
    "lname" : "kohli",
    "age" : 38 ,
    "city" : "mumbai"
}

info.update({"language" : "panjabi"})
print(info)

info.update({"language" : "hindi"})
print(info)

info["language"] = "marathi"
print(info)

#===========================================================
print(info.keys())
print(info.values())
print(info.items())

# ==========================================================

#loops
for k in info.keys():
    print(k)

for v in info.values():
    print(v)

for k,v in info.items():
    print(f"key : {k} , values : {v}")


for K,v in info.items():
    print(f"{k} : {v}")


# ============================================================


info = {
    "fname" : "virat" ,
    "lname" : "kohli",
    "age" : 38 ,
    "city" : "mumbai"
}

dv =info.setdefault("languge" , "hindi")
print(info)
print(dv)



info = {
    "fname" : "virat" ,
    "lname" : "kohli",
    "age" : 38 ,
    "city" : "mumbai"
}

defaults = {
    "language" : "hindi" ,
    "country" : "india" ,
    "course" : "python"
}

for key , values in defaults.items():
    info.setdefault(key , values)

    print(info)



